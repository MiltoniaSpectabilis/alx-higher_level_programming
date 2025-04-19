#!/usr/bin/python3
"""
This module defines a function that serializes an object
and writes it into a file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    This function serializes a specified object and then writes
    it into a specified file
    """
    with open(filename, "w") as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
