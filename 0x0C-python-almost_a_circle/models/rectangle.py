#!/usr/bin/python3
from base import Base
"""
Defines the Rectangle class, inheriting from Base
"""


class Rectangle(Base):
    """
    Representing a rectangle, inheriting ID management from Base.
    Manages width, height and position (x, y).
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle"""
        self.__width = width

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the rectangle"""
        self.__height = height

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x-coordinate of the rectangle"""
        self.__x = x

    @property
    def y(self):
        """Gets the the y-coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y-coordinate of the rectangle"""
        self.__y = y
