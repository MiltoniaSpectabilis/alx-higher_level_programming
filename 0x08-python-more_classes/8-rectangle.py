#!/usr/bin/python3
"""a module that defines a class Rectangle"""


class Rectangle:
    """a class that defines a rectangle"""

    number_of_instances = 0     # keeps track of the num of instances created
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns bigger rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        return max((rect_1, rect_2), key=Rectangle.area)

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
                # convert print_symbol to str so all types can be printed
                row = str(self.print_symbol) * self.width
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
    my_rectangle_1 = Rectangle(8, 4)
    my_rectangle_2 = Rectangle(2, 3)

    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")

    my_rectangle_2.width = 10
    my_rectangle_2.height = 5
    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")

    # my_rec = Rectangle(2, 4)
    # print(f"Area: {my_rec.area()} - Perimeter: {my_rec.perimeter()}")
    # print("--")
    # print("number of instances created: {:d}".format(
    #     Rectangle.number_of_instances))
    # another_my_rec = Rectangle(4, 4)
    # print("number of instances created: {:d}".format(
    #     Rectangle.number_of_instances))
    # del another_my_rec
    # print("number of instances created: {:d}".format(
    #     Rectangle.number_of_instances))
    #
    # my_rec.width = 10
    # my_rec.height = 3
    # my_rec.print_symbol = [1, 2, 3]
    # print(str(my_rec))
    # my_rec.print_symbol = ["C", "is", "fun!"]
    # print(str(my_rec))
    # my_rec.print_symbol = 1
    # print(str(my_rec))
    # print(f"Area: {my_rec.area()} - Perimeter: {my_rec.perimeter()}")
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
