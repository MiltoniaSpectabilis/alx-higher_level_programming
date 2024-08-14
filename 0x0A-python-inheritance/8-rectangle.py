#!/usr/bin/python3
"""Rectangle class."""


class BaseGeometry:
    """A class with area() and integer_validator() methods."""

    def area(self):
        """Raise an Exception with the message "area() is not implemented"."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0."""
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class that represents a rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
