#!/usr/bin/python3
"""
Defines the Rectangle class, inheriting from Base.
"""
from base import Base


class Rectangle(Base):
    """
    Represents a rectangle, inheriting ID management from Base.
    Manages width, height, and position (x, y).
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        # Call the super class constructor to handle the id
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the rectangle."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x-coordinate of the rectangle."""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Gets the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y-coordinate of the rectangle."""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Prints a representation of the rectangle"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end='')
            print("#" * self.width)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args):
        """Updates the instance's attributes"""
        attrs = [
            "id",
            "width",
            "height",
            "x",
            "y"
        ]
        for attr_name, arg in zip(attrs, args):
            setattr(self, attr_name, arg)
