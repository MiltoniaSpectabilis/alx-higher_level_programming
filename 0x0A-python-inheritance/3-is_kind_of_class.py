#!/usr/bin/python3
"""
This module defines a func to check if an obj is an instance of,
or if it is an instance of a subclass of, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if obj is an instance of, or if is
    an instance of a subclass of, a specified class.
    """
    return isinstance(obj, a_class)
