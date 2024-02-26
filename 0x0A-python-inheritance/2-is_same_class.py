#!/usr/bin/python3
"""
Defines is  is_same_class function
"""
def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    parameter
    obj: An object to be checked.
    a_class: A class or type to compare against.

    Returns:
    bool: True if the object is exactly an instance of the specified class;
    otherwise False.
    """
    return type(obj) is a_class
