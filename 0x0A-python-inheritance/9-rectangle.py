#!/usr/bin/python3
"""
This module creates a Rectangle that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns rectangle description
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
