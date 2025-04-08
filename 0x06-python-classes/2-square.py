#!/usr/bin/python3
"""a module that defines a Square class"""


class Square:
    """a class representing a square"""

    def __init__(self, size=0):
        """initialize a Square instance"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
