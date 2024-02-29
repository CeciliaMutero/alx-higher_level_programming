#!/usr/bin/python3
"""
creates a first class Base
"""


class Base:
    """
    Base class for managing ID attribute in all future classes.

    Attributes:
    __nb_objects (int): A private class attribute to keep
    track of the number of objects created.
    id (int): A public instance attribute representing the ID of the object.

    Methods:
    __init__(self, id=None): Constructor method to initialize the Base object.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base object.

        Args:
        id (int, optional): ID to assign to the object.
        If not provided, automatically assigns a unique I
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
