#!/usr/bin/python3
"""
Defines class Rectangle that inherits from Base.
"""


from models.base import Base


class Rectangle(Base):
    """
    A class representing a rectangle.

    Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    x (int): The x-coordinate of the top-left corner of the rectangle.
    y (int): The y-coordinate of the top-left corner of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x(int, optional): The x-coordinate of the top-left corner
        of the rectangle.
        Default is 0.
        y (int, optional): The y-coordinate of the top-left corner
        of the rectangle.
        Default is 0.
        id (int, optional): The unique identifier of the rectangle.
        Default is None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Initializes the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Initializes the height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        initializes the x position of rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets the x position of rectangle.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        initializes the y position of rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets the y position of rectangle.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for _ in range(self.__height):
            print("#" * self.__width)
