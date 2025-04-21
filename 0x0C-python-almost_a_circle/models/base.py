#!/usr/bin/python3
"""
This module creates a Base class for managing object IDs
"""

import json


class Base:
    """
    Base class for managing id attribute in future classes.
    Increments a counter for objects without an explicit id.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance.

        Args:
            id (int, optional): An optional integer id.
                                If None, assigns a unique id based
                                on the number of objects created.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON representation of a list of dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves JSON representation of a list of objects into a file
        """
        list_dicts = []
        if list_objs is None:
            with open(f"{cls.__name__}.json", "w") as f:
                f.write("[]")
        else:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
            with open(f"{cls.__name__}.json", "w") as f:
                f.write(cls.to_json_string(list_dicts))
