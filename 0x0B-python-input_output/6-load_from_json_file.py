#!/usr/bin/python3
"""
This module defines a function that returns a deserialized
object from a string stored in a json file
"""

import json


def load_from_json_file(filename):
    """
    This function fetches the content from a specified json file
    and then returns it deserialized
    """
    with open(filename, "r") as f:
        f_content = f.read()
        obj = json.loads(f_content)
        return obj
