#!/usr/bin/python3
"""BaseGeometry class."""


class BaseGeometry:
    """A class with an area() method that raises an exception."""

    def area(self):
        """Raise an Exception with the message "area() is not implemented"."""
        raise Exception("area() is not implemented")
