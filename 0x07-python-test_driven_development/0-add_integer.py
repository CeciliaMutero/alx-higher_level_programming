#!/usr/bin/python3
"""Defines a function that adds two integers"""


def add_integer(a, b=98):
    """
    function that adds 2 integers.

    parameters:
    a(int)
    b(int) - set to default of 98

    return an integer: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
