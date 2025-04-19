#!/usr/bin/python3
"""
This module defines a function that returns
a deserialized version of the json string passed to it
"""

import json


def from_json_string(my_str):
    """
    returns a deserialized data structure
    """
    py_data_struct = json.loads(my_str)
    return py_data_struct
