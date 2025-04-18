#!/usr/bin/python3
"""
This module defines a func that appends a specified text
to a specified file
"""


def append_write(filename="", text=""):
    """
    Appends a specified text to a specified file
    and returns the number of chars appended
    """
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
