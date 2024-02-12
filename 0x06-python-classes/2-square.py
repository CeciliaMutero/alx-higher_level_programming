#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """
    Represents a square.


    Attributes:
    __size (int): size of the square.
    """

    def __init__(self, size=0):
        """
        initializes private instance attribute.


        Args:
        size(int): The size of the square. Default is 0.

        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
