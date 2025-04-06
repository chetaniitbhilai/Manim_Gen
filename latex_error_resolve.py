import google.generativeai as genai

# Initialize Gemini API (Replace with your actual API key)
genai.configure(api_key="AIzaSyDF1XCJo8Ko6RP6TNgxDGJSDYuydAqw9Ow")

def get_fixed_latex(latex_snippet, error_message):
    """
    Sends the incorrect LaTeX snippet and error message to Gemini and returns a corrected version.

    Args:
        latex_snippet (str): The incorrect LaTeX code.
        error_message (str): The error message from LaTeX compilation.

    Returns:
        str: The corrected LaTeX snippet suggested by Gemini.
    """

    prompt = f"""
    I have a LaTeX snippet that is failing to compile due to an error. Please correct it.

    ### **Original LaTeX Code**
    ```latex
    {latex_snippet}
    ```

    Provide the **corrected** LaTeX **without any explanations or extra text**, just the fixed code inside LaTeX syntax.

    Don't add any extra package. This is for text part in Tex in manim so give accordingly.
    There could be issue of a special charater like \\n for such case add 2 \\ before n.
    """

    try:
        print(prompt)
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(contents=[prompt])
        fixed_latex = response.text.strip()

        # Ensure only the LaTeX code is returned
        if "```latex" in fixed_latex:
            fixed_latex = fixed_latex.split("```latex")[1].split("```")[0].strip()

        return fixed_latex

    except Exception as e:
        print(f"Error contacting Gemini API: {e}")
        return latex_snippet  # Return the original if Gemini fails
