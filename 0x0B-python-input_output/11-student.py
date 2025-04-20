#!/usr/bin/python3
"""
This module creates a Student class
"""


class Student:
    """
    A Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        initializes instance attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns a dictionary containing all data
        of a Student instance
        """
        my_dict = {}
        if isinstance(attrs, list) and \
                all(isinstance(item, str) for item in attrs):
            for item in attrs:
                if item in vars(self):
                    my_dict.update({item: vars(self)[item]})
            return my_dict
        else:
            return vars(self)

    def reload_from_json(self, json):
        """
        clears instance attributes
        and then updates them based on
        the specified dictionary
        """
        vars(self).clear()
        vars(self).update(json)
