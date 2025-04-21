#!/usr/bin/python3
"""
Defines the Square class, inheriting from Rectangle.
"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle.
    """

    def __init__(self,  size, x=0, y=0, id=None):
        """
        Initializes a new Square instance

        Args:
            size (int): The size (width and height) of the square.
            x (int): The x-coordinate of the square's position (default is 0).
            y (int): The y-coordinate of the square's position (default is 0).
            id (int, optional): The id of the square (default is None).
        """
        # Call the super class (Rectangle) constructor,
        # passing size for both width and height.
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns the string representation of the Square.
        Format: [Square] (<id>) <x>/<y> - <size>
        """
        # Either self.width or self.height
        # for size is okay since they are equal
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
