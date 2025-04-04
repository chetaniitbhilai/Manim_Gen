from latex_generator import generate_and_check_latex

def process_latex_data(data):
    """
    Processes LaTeX content from the input dictionary, checks if it compiles, 
    and returns the updated data with compilation status.

    Args:
        data (dict): Dictionary containing LaTeX content.

    Returns:
        dict: Updated dictionary with compilation status for each element.
    """
    data = generate_and_check_latex(data)

    for elem in data['elements']:
        if(elem['content'] is None):
            elem['content']==""
        elem['content'] = [f'"" {line} ""' for line in elem['content']]
        print(elem['content'], "Compilation Status:", elem.get('compilation_status', 'Unknown'))

    return data  # Return the modified data
