#!/usr/bin/python3
"""This module creates a BaseGeometry class"""


class BaseGeometry:
    """A BaseGeometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == '__main__':
    bg = BaseGeometry()
    bg.integer_validator("hamid", 12)

    try:
        bg.integer_validator("hamid", "zahir")
    except Exception as e:
        print(f"{e}")

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print(f"{e}")
