#!/usr/bin/python3
"""
a module that defines a function
that checks if an obj is exactly an instance
of the specified class
"""


def is_same_class(obj, a_class):
    """
    returns True if obj is exactly a_class otherwise returns False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
