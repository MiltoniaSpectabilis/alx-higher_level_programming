#!/usr/bin/python3
"""
This module defines a function that returns a serialized
version of the object passed to it
"""

import json


def to_json_string(my_obj):
    """
    returns a serialized/jsonified version of the object
    """
    json_str = json.dumps(my_obj)
    return json_str
