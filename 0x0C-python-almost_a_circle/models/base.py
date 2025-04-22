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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a deserialized list of a JSON string representation
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with attributes already set from a dictionary
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 2)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a JSON file.

        The filename is based on the class name
        (e.g., Rectangle.json, Square.json).
        Reads the JSON string from the file,
        converts it to a list of dictionaries,
        and then creates instances from those dictionaries.

        Returns:
            list: A list of instances of the calling class (cls),
                  or an empty list if the file does not exist.

        """
        try:
            with open(f"{cls.__name__}.json", "r") as f:
                f_content = f.read()
            list_dicts = cls.from_json_string(f_content)
            list_instances = []
            for dic in list_dicts:
                list_instances.append(cls.create(**dic))
            return list_instances
        except FileNotFoundError:
            return []
