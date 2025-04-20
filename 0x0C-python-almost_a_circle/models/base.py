#!/usr/bin/python3
"""
This module creates a Base class for managing object IDs
"""


class Base:
    """
    Base class for managing id attribute in future classes.
    Increments a counter for objects without an explicit id.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance.

        Args:
            id (int, optional): An optional integer id.
                                If None, assigns a unique id based
                                on the number of objects created.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
