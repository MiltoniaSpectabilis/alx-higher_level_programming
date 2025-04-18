#!/usr/bin/python3
"""
This module implements a function that
reads and prints the content of a file
"""


def read_file(filename=""):
    """reads and prints the content of the file"""
    with open(f"{filename}", "r") as file:
        file_content = file.read()
        print(file_content)
