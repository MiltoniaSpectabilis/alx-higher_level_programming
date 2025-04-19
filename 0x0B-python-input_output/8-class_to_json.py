#!/usr/bin/python3
"""
This module defines a function that fetches
a specified object data (attributes and their values)
and returns them in dictionary format
"""


def class_to_json(obj):
    """
    This function fetches the object's data
    and returns it in a dictionary
    """
    dict = {}
    for attr_name, attr_val in vars(obj).items():
        dict.update({attr_name: attr_val})
    return dict
