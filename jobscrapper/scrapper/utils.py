# utils.py
from typing import List


def data_sanitizer(data_list) -> List:
    """
    data_sanitizer is a function to clean the html element inner text.
    the inner text html elemenets come with several spaces and break lines,
    this sanitizer deletes those innecesary spaces.
    Parameters:
        - data_list: List | list of the elements to sanitize
    Returns:
        - sanitized_data: List | list of the sanitized elemenets
    """
    sanitized_data = []
    for data in data_list:
        txt = data.get_text()
        txt = "".join([str(x) for x in txt if str(x)])
        txt = txt.strip()
        sanitized_data.append(txt)
    return sanitized_data
