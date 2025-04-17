#!/usr/bin/python3
"""
This module checks if an obj inherits from a specified class
"""


def inherits_from(obj, a_class):
    """Checks if an obj inherits from a specified class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
