#!/usr/bin/python3
"""a module that defines a class Rectangle"""


class Rectangle:
    """a class that defines a rectangle"""

    number_of_instances = 0     # keeps track of the num of instances created

    def __init__(self, width=0, height=0):
        """attribute initialization"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return rec
        else:
            for _ in range(self.height):
                row = "#" * self.width
                rec += row
                if _ < self.height - 1:
                    rec += '\n'
            return rec

    def __repr__(self):
        """returns a str that recreates the object for devs"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """deletes instance and prints message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


if __name__ == "__main__":
    my_rec = Rectangle(2, 4)
    print(f"Area: {my_rec.area()} - Perimeter: {my_rec.perimeter()}")
    print("--")
    print("number of instances created: {:d}".format(
        Rectangle.number_of_instances))
    another_my_rec = Rectangle(4, 4)
    print("number of instances created: {:d}".format(
        Rectangle.number_of_instances))
    del another_my_rec
    print("number of instances created: {:d}".format(
        Rectangle.number_of_instances))

    # my_rec.width = 10
    # my_rec.height = 3
    # print(f"Area: {my_rec.area()} - Perimeter: {my_rec.perimeter()}")
    # print(str(my_rec))
    # my_rec.width = 1
    # my_rec.height = 1
    # print(str(my_rec))
    # my_rec = Rectangle(0, 0)
    # print(str(my_rec))
    # print(repr(my_rec))
    # print(repr(Rectangle(1, 2)))
    # my_rec = Rectangle(5, 5)
    # new_rec = eval(repr(my_rec))
    # print(str(new_rec))
    # print(repr(new_rec))
    # print(my_rec is new_rec)
    # print(type(my_rec) is type(new_rec))
    # del my_rec
    # try:
    #     print(my_rec)
    # except Exception as e:
    #     print("[{}] {}".format(e.__class__.__name__, e))
