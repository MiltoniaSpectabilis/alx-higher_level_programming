#!/usr/bin/python3
"""
This module creates a Square that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializer a new Square inrtance
        """
        # checks whether attr size is a positive int
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        returns the area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        returns square description
        """
        return f"[Square] {self.__size}/{self.__size}"
