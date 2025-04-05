import os
import subprocess
import shutil
import glob
import time
from latex_error_resolve import get_fixed_latex  # Replace with actual function to call Gemini API

TEMPLATE = r"""
\documentclass[preview]{standalone}
\usepackage[english]{babel}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{mathrsfs}
\begin{document}
\begin{center}
{content}
\end{center}
\end{document}
"""

def compile_latex(filename):
    """Compile LaTeX file using pdflatex and capture errors"""
    try:
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', filename],
            capture_output=True, text=True, timeout=300
        )
        if result.returncode != 0:
            return False, result.stderr  # Return False and errors
        else:
            return True, ""  # Compilation successful
    except subprocess.TimeoutExpired:
        return False, "Compilation timed out."
    except FileNotFoundError:
        return False, "pdflatex not found. Make sure LaTeX is installed."

def generate_and_check_latex(data, output_dir="latex_files", cleanup=True, max_retries=3):
    """
    Generates, compiles, and fixes LaTeX files using Gemini.

    Parameters:
        data (dict): Input data containing LaTeX content.
        output_dir (str): Directory where LaTeX files will be stored.
        cleanup (bool): Whether to delete files after processing.
        max_retries (int): Maximum times to attempt fixing LaTeX issues.

    Returns:
        dict: Updated data with compilation status and errors.
    """

    os.makedirs(output_dir, exist_ok=True)

    for element in data["elements"]:
        element["compilation_status"] = []
        element["compilation_errors"] = []

    # Generate LaTeX files
    for idx, element in enumerate(data["elements"]):
        for line_idx, line in enumerate(element["content"]):
            filename = os.path.join(output_dir, f"element_{idx+1}_line_{line_idx+1}.tex")
            latex_code = TEMPLATE.replace("{content}", line)

            with open(filename, "w", encoding="utf-8") as f:
                f.write(latex_code)

            # Compile LaTeX
            success, error_message = compile_latex(filename)
            element["compilation_status"].append(success)
            element["compilation_errors"].append(error_message)

            # Retry up to max_retries if compilation fails
            retries = 0
            while not success and retries < max_retries:
                print(f"Fixing LaTeX for {filename} (Attempt {retries + 1})")

                # Send to Gemini for fixing
                fixed_latex = get_fixed_latex(line, error_message)

                # Update the LaTeX content and retry
                latex_code = TEMPLATE.replace("{content}", fixed_latex)
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(latex_code)

                success, error_message = compile_latex(filename)
                retries += 1

                if success:
                    element["content"][line_idx] = fixed_latex  # Update content with corrected version
                    element["compilation_status"][line_idx] = True
                    element["compilation_errors"][line_idx] = ""
                    break  # Stop retrying if fixed

            # If still fails after max retries, remove the element
            if not success:
                print(f"Failed after {max_retries} retries. Removing {filename} from dataset.")
                element["compilation_status"][line_idx] = False
                element["compilation_errors"][line_idx] = error_message
                element["content"][line_idx] = ""  # Mark for removal
                element["speak"][line_idx] = ""

    # Remove elements that couldn't be fixed
    for element in data["elements"]:
        element["content"] = [c for c in element["content"] if c]
        element["compilation_status"] = [s for s in element["compilation_status"] if s]
        element["compilation_errors"] = [e for e in element["compilation_errors"] if e == ""]

    # Cleanup: Remove all files from the output directory
    if cleanup:
        for file in os.listdir(output_dir):
            file_path = os.path.join(output_dir, file)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

        # Remove the output directory itself
        try:
            os.rmdir(output_dir)
            print(f"Deleted '{output_dir}' and all generated files.")
        except OSError:
            print(f"Could not delete '{output_dir}', directory not empty.")

    return data








# import os
# import subprocess
# import shutil
# import glob
# import time
# from latex_error_resolve import get_fixed_latex  # Replace with actual function to call Gemini API

# TEMPLATE = r"""
# \documentclass[preview]{standalone}
# \usepackage[english]{babel}
# \usepackage{amsmath}
# \usepackage{amssymb}
# \usepackage{mathrsfs}
# \begin{document}
# \begin{center}
# {content}
# \end{center}
# \end{document}
# """

# def compile_latex(filename):
#     """Compile LaTeX file using pdflatex and capture errors"""
#     try:
#         result = subprocess.run(
#             ['pdflatex', '-interaction=nonstopmode', filename],
#             capture_output=True, text=True, timeout=300
#         )
#         if result.returncode != 0:
#             return False, result.stderr  # Return False and errors
#         else:
#             return True, ""  # Compilation successful
#     except subprocess.TimeoutExpired:
#         return False, "Compilation timed out."
#     except FileNotFoundError:
#         return False, "pdflatex not found. Make sure LaTeX is installed."

# def generate_and_check_latex(data, output_dir="latex_files", cleanup=True, max_retries=3):
#     """
#     Generates, compiles, and fixes LaTeX files using Gemini.

#     Parameters:
#         data (dict): Input data containing LaTeX content.
#         output_dir (str): Directory where LaTeX files will be stored.
#         cleanup (bool): Whether to delete files after processing.
#         max_retries (int): Maximum times to attempt fixing LaTeX issues.

#     Returns:
#         dict: Updated data with compilation status and errors.
#     """

#     os.makedirs(output_dir, exist_ok=True)

#     for element in data["elements"]:
#         element["compilation_status"] = []
#         element["compilation_errors"] = []

#     # Generate LaTeX files
#     for idx, element in enumerate(data["elements"]):
#         for line_idx, line in enumerate(element["content"]):
#             filename = os.path.join(output_dir, f"element_{idx+1}_line_{line_idx+1}.tex")
#             latex_code = TEMPLATE.replace("{content}", line)

#             with open(filename, "w", encoding="utf-8") as f:
#                 f.write(latex_code)

#             # Compile LaTeX
#             success, error_message = compile_latex(filename)
#             element["compilation_status"].append(success)
#             element["compilation_errors"].append(error_message)

#             # Retry up to max_retries if compilation fails
#             retries = 0
#             while not success and retries < max_retries:
#                 print(f"Fixing LaTeX for {filename} (Attempt {retries + 1})")

#                 # Send to Gemini for fixing
#                 fixed_latex = get_fixed_latex(line, error_message)

#                 # Update the LaTeX content and retry
#                 latex_code = TEMPLATE.replace("{content}", fixed_latex)
#                 with open(filename, "w", encoding="utf-8") as f:
#                     f.write(latex_code)

#                 success, error_message = compile_latex(filename)
#                 retries += 1

#                 if success:
#                     element["content"][line_idx] = fixed_latex  # Update content with corrected version
#                     element["compilation_status"][line_idx] = True
#                     element["compilation_errors"][line_idx] = ""
#                     break  # Stop retrying if fixed

#             # If still fails after max retries, remove the element
#             if not success:
#                 print(f"Failed after {max_retries} retries. Removing {filename} from dataset.")
#                 element["compilation_status"][line_idx] = False
#                 element["compilation_errors"][line_idx] = error_message
#                 element["content"][line_idx] = ""  # Mark for removal
#                 element["speak"][line_idx]= ""

#     # Remove elements that couldn't be fixed
#     for element in data["elements"]:
#         element["content"] = [c for c in element["content"] if c is not None]
#         element["compilation_status"] = [s for s in element["compilation_status"] if s]
#         element["compilation_errors"] = [e for e in element["compilation_errors"] if e == ""]

#     # Cleanup files
#     if cleanup:
#         for ext in ["*.aux", "*.log", "*.pdf", "*.out"]:
#             for file in glob.glob(os.path.join(output_dir, ext)):
#                 os.remove(file)
#         shutil.rmtree(output_dir)
#         print(f"Deleted '{output_dir}' and all generated files.")

#     return data




