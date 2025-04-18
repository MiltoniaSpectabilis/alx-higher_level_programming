#!/usr/bin/python3
"""
This module defines a function writes a specified text
to a specified file
"""


def write_file(filename="", text=""):
    """
    writes a specified text to a specified file
    and returns the number of written chars
    """
    with open(filename, "w") as f:
        f.write(text)

    return len(text)
