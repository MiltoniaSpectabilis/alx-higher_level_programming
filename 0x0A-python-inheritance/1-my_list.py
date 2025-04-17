#!/usr/bin/python3
"""a module that prints a sorted list"""


class MyList(list):
    """a class that inherits from list"""

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
