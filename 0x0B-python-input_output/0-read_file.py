#!/usr/bin/python3
"""
Reads a text file.
"""


def read_file(filename=""):
    """
    Read and print the content of a text file to stdout.

    Parameters:
    filename (str): file to be read. Default is an empty string.

    Returns:
    None
    """
    with open(filename, 'r', encoding='UTF8') as file:
        content = file.read()
        print(content, end="")
