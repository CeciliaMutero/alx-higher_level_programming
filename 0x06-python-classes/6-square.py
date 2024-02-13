#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """
    Represents a square.


    Attributes:
    __size (int): size of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initializes private instance attribute.


        Args:
        size(int): The size of the square. Default is 0.
        position: position of the square.

        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Retrieves position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(x, int) and x >= 0 for x in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
