#!/usr/bin/python3
"""
appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF8) and
    return the number of characters appended.

    Parameters:
    filename (str): The name of the file to append to.
    Default is an empty string
    text (str): string to append to the file. Default is an empty string.

    Returns:
    int: The number of characters appended to the file.
    """
    with open(filename, 'a', encoding='UTF8') as file:
        content = file.write(text)
        return content
