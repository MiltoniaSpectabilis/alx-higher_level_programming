#!/usr/bin/python3
"""a module that defines a Square class"""


class Square:
    """a class representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a Square instance"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) == 0
                and all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for row in range(self.__size):
            print(f"{' ' * self.__position[0]}", end='')
            for item in range(self.__size):
                print("#", end='')
            print()
