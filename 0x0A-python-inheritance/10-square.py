#!/usr/bin/python3
"""Square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square."""

    def __init__(self, size):
        """Initialize a Square instance."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
