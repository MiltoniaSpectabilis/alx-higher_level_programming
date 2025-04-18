#!/usr/bin/python3
"""
This module implements a function that
reads and prints the content of a file
"""


def read_file(filename=""):
    """reads and prints the content of the file"""
    with open(filename, "r") as f:
        content = f.read()
        print(content, end='')  # remove new line at the end of content
