#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script-code.py

A script that:
  1. Uses Google Generative AI to process a local video file (e.g. sample.webm),
     extract transcriptions in an XML-like format,
  2. Extracts slide content from the transcription,
  3. Generates structured JSON (with "content" and "speak" fields) for a Manim scene,
  4. Optionally generates Manim scene code.
  
Usage:
    python3 script-code.py <video_file>
"""

import sys
import os
import time
import ast
import re
import subprocess
from check import process_latex_data
from repeated import check_repeated_content


import numpy as np
from manim import *  # Ensure manim is installed

#############################################
# Section 1: Utility Functions
#############################################

# def generate_manim_code(title, elements):
#     """Generates Manim scene code based on a title and a list of elements."""
#     code = f"""
# from manim import *
# config.tex_template.add_to_preamble(r"\\usepackage{{mathrsfs}}")

# class GeneratedScene(MovingCameraScene):
#     def get_final_camera_setup(self):
#         # Create all mobjects first
#         title = Tex(r"{title}", font_size=50).to_edge(UP)
#         content_elements = [title]
#         prev_mobject = title
# """
#     # Generate code for each element
#     for idx, elem in enumerate(elements):
#         elem_type = elem['type']
#         content_lines = elem['content']
#         content_args = ", ".join([f'r"{line}"' for line in content_lines])
#         # Use Tex for 'tex' type and MathTex for math content
#         class_name = "Tex" if elem_type == "tex" else "MathTex"
#         font_size = 40 if elem_type == "tex" and idx < 2 else (36 if elem_type == "tex" else 40)
#         code += f"""
#         element{idx} = {class_name}({content_args}, font_size={font_size}).next_to(prev_mobject, DOWN, buff=0.5)
#         content_elements.append(element{idx})
#         prev_mobject = element{idx}
# """
#     code += f"""
#         # Group all content elements
#         content = VGroup(*content_elements)
#         self.add(title)
#         title.set_opacity(0)
#         self.camera.auto_zoom([title], margin=1)
#         current_content = [title]
#         for element in content_elements[1:]:
#             self.add(element)
#             element.set_opacity(0)
#             current_content.append(element)
#         self.play(
#             self.camera.auto_zoom(
#                 content,
#                 margin=0.5,
#                 animate=True
#             ).build(),
#             run_time=2
#         )
#         self.camera.frame.save_state()
#         self.camera.auto_zoom(content, margin=0.5)
#         final_frame_center = self.camera.frame.get_center()
#         final_focal_width = self.camera.frame.get_width()
#         self.camera.frame.restore()
#         return final_frame_center, final_focal_width

#     def construct(self):
#         # Get the final camera settings from a silent run
#         final_center, final_width = self.get_final_camera_setup()
#         title = Tex(r"{title}", font_size=50).to_edge(UP)
#         content_elements = [title]
#         prev_mobject = title
# """
#     for idx, elem in enumerate(elements):
#         elem_type = elem['type']
#         content_lines = elem['content']
#         content_args = ", ".join([f'r"{line}"' for line in content_lines])
#         class_name = "Tex" if elem_type == "tex" else "MathTex"
#         font_size = 40 if elem_type == "tex" and idx < 2 else (36 if elem_type == "tex" else 40)
#         code += f"""
#         element{idx} = {class_name}({content_args}, font_size={font_size}).next_to(prev_mobject, DOWN, buff=0.5)
#         content_elements.append(element{idx})
#         prev_mobject = element{idx}
# """
#     code += """
#         content = VGroup(*content_elements)
#         self.camera.frame.move_to(final_center)
#         self.camera.frame.set_width(final_width)
#         self.play(Write(title))
#         self.wait(1)
# """
#     for idx in range(len(elements)):
#         code += f"""
#         self.play(Write(element{idx}))
#         self.wait(1)
# """
#     code += """
#         self.wait(2)
# """
#     return code

def generate_manim_code(title, elements=None):
    # Static data for Empty Index Sets

    code = f"""
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
config.tex_template.add_to_preamble(r"\\usepackage{{mathrsfs}}")

class GeneratedScene(VoiceoverScene, MovingCameraScene):
    def get_final_camera_setup(self):
        self.set_speech_service(GTTSService())

        # Create all mobjects first
        title = Tex(r"{title}", font_size=50).to_edge(UP)
        content_elements = [title]
        prev_mobject = title
    """

    for idx, elem in enumerate(elements):
        elem_type = elem['type']
        content_lines = elem['content']
        speech_text = elem['speak']
        content_args = ", ".join([f'r"{line}"' for line in content_lines])
        if(content_args is None):
            content_args = ""
        class_name = "Tex" if elem_type == "tex" else "MathTex"
        font_size = 40 if elem_type == 'tex' and idx < 2 else 36

        code += f"""
        element{idx} = {class_name}({content_args}, font_size={font_size}).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element{idx})
        prev_mobject = element{idx}
"""

    code += """
        # Group all elements
        content = VGroup(*content_elements)

        # Initial camera setup with title
        self.add(title)
        title.set_opacity(0)
        self.camera.auto_zoom([title], margin=1)

        # Add content progressively with camera adjustments
        current_content = [title]
        for element in content_elements[1:]:
            self.add(element)
            element.set_opacity(0)
            current_content.append(element)

        # Final adjustment for all content
        self.play(
            self.camera.auto_zoom(
                content, margin=0.5, animate=True
            ).build(),
            run_time=2
        )

        self.camera.frame.save_state()
        self.camera.auto_zoom(content, margin=0.5)

        # Extract final camera settings
        final_center = self.camera.frame.get_center()
        final_width = self.camera.frame.get_width()

        # Restore initial camera state
        self.camera.frame.restore()

        return final_center, final_width

    def construct(self):
        final_center, final_width = self.get_final_camera_setup()

        # Create content again for the actual animation
        title = Tex(r"{title}", font_size=50).to_edge(UP)
        content_elements = [title]
        prev_mobject = title
""".format(title=title)

    for idx, elem in enumerate(elements):
        elem_type = elem['type']
        content_lines = elem['content']
        speech_text = elem['speak'][0] if isinstance(elem['speak'], list) else elem['speak']
        content_args = ", ".join([f'r"{line}"' for line in content_lines])
        class_name = "Tex" if elem_type == "tex" else "MathTex"
        font_size = 40 if elem_type == 'tex' and idx < 2 else 36

        code += f"""
        element{idx} = {class_name}({content_args}, font_size={font_size}).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element{idx})
        prev_mobject = element{idx}
"""

    code += """
        # Group all elements
        content = VGroup(*content_elements)

        # Apply final camera settings before animations start
        self.camera.frame.move_to(final_center)
        self.camera.frame.set_width(final_width)

        # Animate content with voiceover
        with self.voiceover(text=r"{title}"):
            self.play(Write(title))
            self.wait(1)
""".format(title=title)

    for idx, elem in enumerate(elements):
        speech_text = elem['speak'][0] if isinstance(elem['speak'], list) else elem['speak']
        code += f"""
        with self.voiceover(text=r"{speech_text}"):
            self.play(Write(element{idx}))
            self.wait(1)
"""

    code += """
        self.wait(2)
"""

    return code





def convert_string_to_dict(input_str):
    """
    Converts a JSON-like string (with unquoted keys) into a Python dictionary.
    Expected format:
    {
      title : "Some Title",
      elements : [
          {"type": "tex", "content": ["..."], "speak": ["..."]},
          ...
      ]
    }
    Also escapes ampersands to prevent LaTeX errors.
    """
    cleaned_str = input_str.strip().strip('`').replace('json\n', '')
    parsed_dict = ast.literal_eval(cleaned_str)
    # Escape ampersands in all content and speak strings.
    for elem in parsed_dict["elements"]:
        elem["content"] = [item.replace("&", r"\&") for item in elem["content"]]
        elem["speak"] = [item.replace("&", r"\&") for item in elem["speak"]]
    return {
        "title": parsed_dict["title"],
        "elements": [
            {
                "type": elem["type"],
                "content": elem["content"],
                "speak": elem["speak"]
            }
            for elem in parsed_dict["elements"]
        ]
    }

def extract_slide_content(xml_string):
    """
    Extracts slide content from an XML-like string.
    For example, given:
        <content>
            <slide1>Text from slide 1</slide1>
            <slide2>Text from slide 2</slide2>
        </content>
    it returns a list like ["Text from slide 1", "Text from slide 2"].
    """
    pattern = re.compile(r'<slide\d+>(.*?)</slide\d+>', re.DOTALL)
    return pattern.findall(xml_string)

#############################################
# Section 2: Google Generative AI Integration
#############################################
# IMPORTANT: Ensure you have installed the official google-generativeai package:
#   pip install google-generativeai

import google.generativeai as genai
# from google import genai

# Configure the API key (there's no Client class in the new version)
API_KEY = "AIzaSyDF1XCJo8Ko6RP6TNgxDGJSDYuydAqw9Ow"
genai.configure(api_key=API_KEY)

# Import file functions; the current version uses upload_file.
from google.generativeai import files

#############################################
# Section 3: Video File Processing and Transcription
#############################################
def process_video(video_path):
    """
    Uploads a video file, waits for processing, and returns the file object.
    """
    print("Uploading file:", video_path)

    
    # Correct file upload method
    video_file = genai.upload_file(path=video_path)
    
    print(f"Completed upload: {video_file.uri}")
    print("File metadata:", video_file.video_metadata)
    
    # Wait for processing
    print("Waiting for processing", end='')
    while video_file.state.name == "PROCESSING":
        # print('.', end='', flush=True)
        time.sleep(5)
        video_file = genai.get_file(video_file.name)
    
    if video_file.state.name != "ACTIVE":
        raise ValueError(f"Video processing failed with state: {video_file.state.name}")
    
    print("\nFile processing completed successfully")
    return video_file

def transcribe_video(video_file, prev_latex):
    """
    Generates a transcription for the given video file using a Gemini model.
    """
    prompt2vid2text = '''This is a video of a teacher explaining mathematical concepts on sheets of paper. 
    Your task is to extract and transcribe the exact content written on each sheet.
    Guidelines:
    - Use LaTeX for anything related to mathematics including equations, formulas.
    - Do not add any extra explanation.
    - Provide the output in the following XML-like format:
    <content>
        <slide1>Extracted content from Slide 1</slide1>
        <slide2>Extracted content from Slide 2</slide2>
        <slide3>Extracted content from Slide 3</slide3>
        ...
    </content>
    if it is a mathematical equation use \\( equation \\)  or \\[ equation \\] instead of $ $. Don't use $ math $ in any case. Use only \\( \\) or \\[  \\].
    Ensure there is proper spacing between \\( \\) and the text left to it. 

    Example 1:
    Right Ex.1. Let \\(\\{ E_n \\}\\) be a disjoint sequence of sets. Applying the definition of \\(\\limsup\\) and \\(\\liminf\\), we note that there are no elements of \\(\\Omega\\) which 
    belong to two sets as the sets are disjoint. Hence, \\(E_{*} = E^{*} = \\varnothing\\).
    instead of 
    Wrong Ex.1. Let \\{ E_{n} \\} be a disjoint seq. of sets. Applying the definition of $\\lim \\sup$ and $\\lim \\inf$, we note that these are no elements of $\\Omega$ which                        
    belong to two sets as the sets are disjoint. Hence $E_{*} = E^{*} = \\phi$.

    Example 2:
    Right Ex 2: 
    If we consider \\( x \\in \\Omega \\).
    instead of 
    Wrong Ex 2:
    If we consider x belongs to x \\in \\Omega.

    Don't include any symbol that is there from any other external package like mathrsfs. Rather use simple alphabetical variables.
    Also to note if there is \\n then do not forget to add another \\ otherwise it will go in multiple lines while compiling like in \\notin 
    '''

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(contents=[video_file, prompt2vid2text])
    print("Transcription response:")
    print(response.text)
    return response.text

#############################################
# Section 4: Generate Structured JSON for Manim
#############################################
def generate_json_for_manim(slide_text):
    """
    Uses a Gemini model to produce JSON (with 'speak' field) for a Manim scene,
    based on slide text and a prompt.
    """
    prompt = """Write this in the given format only dont write anything else json format only
{
title : "Introduction to Fourier Transform"
elements : [
    {"type": "tex", "content": ["The Fourier Transform decomposes a function"], "speak":["The Fourier Transform decomposes a function."]},
    {"type": "tex", "content": [r"$\\Omega$ $\\rightarrow$ space or universal set"], "speak":["into its frequency components."]},
    {"type": "tex", "content": ["It is widely used in signal processing."], "speak":["It is widely used in signal processing."]},
    {"type": "tex", "content": [r"4. \\( X_{E\\triangle F}(x) = \\left| X_E(x) - X_F(x) \\right| = X_E(x) + X_F(x) \\mod 2 \\)"], "speak":["explain the equation"]},
    {"type": "tex", "content": [r"Let \\(\\{E_n\\}\\) be a disjoint sequence of sets. Applying the definition of \\(\\limsup\\) and \\(\\liminf\\), we note that there are no elements of \\(\\Omega\\) which belong to two sets as the sets are disjoint. Hence, \\(E_{*} = E^{*} = \\varnothing\\)."], "speak":["explain the equation"]}
]
}
RETURN your answer in the given format
{
  title: str,
  elements: list of dictionary(with keys type, content, and speak)
}
Give everything in Tex format only. 
"""
    combined_input = slide_text + "  " + prompt + " "
    print("\n\n\nCOMBINED INPUT\n\n",slide_text)
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(contents=combined_input)
    print("JSON response:")
    print(response.text)
    result = convert_string_to_dict(response.text)
    return result

#############################################
# Section 5: Main Execution Flow
#############################################
def main():
    ## getting the previous generated latex
    prev_latex_path = "prev_latex.txt"
    try:
        with open(prev_latex_path, "r", encoding="utf-8") as f:
            prev_latex_content = f.read()
    except FileNotFoundError:
        print("Previous LaTeX file not found. Proceeding without it.")
        prev_latex_content = ""


    # Expect the local video file path as a command-line argument
    if len(sys.argv) < 2:
        # print("Usage: python3 script-code.py <video_file>")
        sys.exit(1)
    video_path = sys.argv[1]
    
    # Process video and get transcription
    video_file = process_video(video_path)
    transcription_text_temp = transcribe_video(video_file, prev_latex_content)
    

    # transcription_text = check_repeated_content(transcription_text_temp)
    
    print("This is the non repeating transcription text\n\n\n\n\n" ,transcription_text_temp, "\n\n\n\n\n\n")
    # Extract slide content from transcription
    slides = extract_slide_content(transcription_text_temp)
    print("Extracted slides:", slides)
    if len(slides) == 0:
        print("No slides extracted. Exiting.")
        sys.exit(1)
    
    # writing previous latex in that file
    with open(prev_latex_path, "w", encoding="utf-8") as f:
        for slide in slides:
            f.write(slide)

    # Use the second slide (if available) for generating JSON, otherwise the first slide.
    slide_for_json=""
    for slide in slides:
        slide_for_json+=slide
    # slide_for_json = slides[1] if len(slides) > 1 else slides[0]
    structured_result_temp = generate_json_for_manim(slide_for_json)
    
    structured_result=process_latex_data(structured_result_temp)



    print(structured_result)
    # # Extract title and elements from the structured JSON
    title = structured_result["title"]
    elements = structured_result["elements"]
    for elem in elements:
        print("Content:", elem['content'])
        # Optionally print the speak field:
        # print("Speak:", elem['speak'])



    # (Optional) Generate Manim scene code and save to a file
    manim_code = generate_manim_code(title, elements)
    with open("generated_scene.py", "w") as f:
        f.write(manim_code)
    print("Manim scene code saved to generated_scene.py")
    

    # (Optional) Run the generated scene using subprocess (if desired)
    # Uncomment the following lines to render the scene:
    import subprocess
    import shutil
    subprocess.run(["python3", "-m", "manim", "-qh", "generated_scene.py", "GeneratedScene"], check=True)
    # After rendering the Manim scene
    manim_output_dir = os.path.join("media", "videos", "generated_scene", "1080p60")
    generated_video_path = os.path.join(manim_output_dir, "GeneratedScene.mp4")
    destination_path = os.path.join("media", "videos", "GeneratedScene.mp4")

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    # Copy the generated video to the expected location
    if os.path.exists(generated_video_path):
        shutil.copy(generated_video_path, destination_path)
    else:
        print(f"Error: Generated video not found at {generated_video_path}")
    
if __name__ == '__main__':
    main()
