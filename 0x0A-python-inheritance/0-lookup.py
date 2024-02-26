#!/usr/bin/python3
"""
Returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Retrieve a list of available methods and
    attributes associated with the given object.

    Parameters:
    obj (object): retrieve available methods and attributes.

    Returns:
    list of str: A list containing the names of available methods and
    attributes associated with the given object.
    """
    return dir(obj)
