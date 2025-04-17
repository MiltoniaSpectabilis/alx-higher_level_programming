#!/usr/bin/python3
"""
This module defines a func to check if an obj is an instance of,
or if it is an instance of a subclass of, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    checks if an object is an instance of, or if it is an instance
    of a subclass of, a specified class.
    """
    return True if isinstance(obj, a_class) else False
