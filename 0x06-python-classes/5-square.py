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

    @property
    def size(self):
        """
        Retrieves size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size to value.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #.
        """
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print("#" * self.__size)
