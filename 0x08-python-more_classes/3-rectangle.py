#!/usr/bin/python3
"""a module that defines a class Rectangle"""


class Rectangle:
    """a class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """attribute initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """return rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.height + self.width)

    def __str__(self):
        """returns a representation of a rectangle with '#'"""
        rec = ""
        if self.width != 0 or self.height:
            for _ in range(self.height):
                row = "#" * self.width
                rec += row
                if _ < self.height - 1:
                    rec += '\n'
            return rec
        else:
            return ""


if __name__ == "__main__":
    my_rec = Rectangle(2, 4)
    print(f"Area: {my_rec.area()} - Perimeter: {my_rec.perimeter()}")
    print("--")
    my_rec.width = 10
    my_rec.height = 3
    print(f"Area: {my_rec.area()} - Perimeter: {my_rec.perimeter()}")
    print(str(my_rec))
    my_rec.width = 1
    my_rec.height = 1
    print(str(my_rec))
