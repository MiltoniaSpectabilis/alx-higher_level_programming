#!/usr/bin/python3
"""Exact same object function."""


def is_same_class(obj, a_class):
    """
    Return True if the object is exactly an instance of the specified class.
    """
    return type(obj) is a_class
