#!/usr/bin/python3
"""A module that prints a square with the char '#'"""


def print_square(size):
    """prints a square using '#'"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)


if __name__ == '__main__':
    print_square()
    print_square("abc")
    print_square(-1)
