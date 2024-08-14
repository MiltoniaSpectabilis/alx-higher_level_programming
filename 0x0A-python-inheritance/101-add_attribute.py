#!/usr/bin/python3
"""Add attribute function."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if it's possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
