#!/usr/bin/python3
"""
writes a string to a text file
"""


def write_file(filename="", text=""):
    """"
    Write a string to a text file (UTF8) and
    return the number of characters written.

    Parameters:
    filename (str): file to write to. Default is an empty string.
    text (str): string to write to the file. Default is an empty string.

    Returns:
    int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='UTF8') as file:
        content = file.write(text)
        return content
