import google.generativeai as genai

# Configure Gemini API (Make sure to set up authentication)
genai.configure(api_key="AIzaSyDF1XCJo8Ko6RP6TNgxDGJSDYuydAqw9Ow")  # Replace with your actual API key

def generate_gemini_prompt(prev_content, new_content):
    """Formats the prompt for Gemini to filter out repeated content."""
    prompt = f"""You are given two XML-like content chunks. 
The first chunk is from the previous part of the video, and the second chunk is the newly generated content. 
Please remove any content from the new chunk that is already present in the previous chunk while maintaining the original XML structure.

### Previous Chunk:
{prev_content}

### New Chunk:
{new_content}

### Instructions:
- Remove any repeated content from the new chunk.
- Maintain the original XML-like structure.
- Do not introduce new information.
- Return the filtered content in the same XML-like format.

### Output (Filtered Content):
"""
    return prompt

def filter_content_with_gemini(prev_chunk, new_chunk):
    """Calls Gemini API to filter out repeated content."""
    model = genai.GenerativeModel("gemini-2.0-flash")  # Initialize model
    prompt_text = generate_gemini_prompt(prev_chunk, new_chunk)

    response = model.generate_content(prompt_text)
    
    if response and response.text:
        return response.text    
    else:
        print("Error: No response from Gemini.")
        return new_chunk  # Return new chunk unchanged if Gemini fails

def read_previous_chunk(file_path="prev_latex.txt"):
    """Reads the previous chunk from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""  # If the file doesn't exist, assume no previous content

def save_new_chunk(new_chunk, file_path="prev_latex.txt"):
    """Saves the new chunk for future comparisons."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_chunk)

def check_repeated_content(new_chunk, file_path="prev_latex.txt"):
    """
    Reads the previous video chunk, filters out duplicates using Gemini,
    updates the stored chunk, and returns the filtered content.
    """
    prev_chunk = read_previous_chunk(file_path)  # Read existing chunk
    filtered_content = filter_content_with_gemini(prev_chunk, new_chunk)  # Filter new chunk
    save_new_chunk(new_chunk, file_path)  # Save the updated chunk for future comparisons
    return filtered_content  # Return the cleaned-up content
