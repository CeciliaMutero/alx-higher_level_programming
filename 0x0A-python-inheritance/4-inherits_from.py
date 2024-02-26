#!/usr/bin/python3
"""
Define inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    parameter
    obj: An object to be checked.
    a_class: A class or type to compare against.

    Returns:
    bool: True if the object is exactly an instance of the specified class;
    otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
