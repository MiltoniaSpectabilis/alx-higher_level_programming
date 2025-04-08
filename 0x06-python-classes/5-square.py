#!/usr/bin/python3
"""a module that defines a Square class"""


class Square:
    """a class representing a square"""

    def __init__(self, size=0):
        """initialize a Square instance"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for row in range(self.__size):
            for item in range(self.__size):
                print("#", end='')
            print()
