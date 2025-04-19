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

    def to_json(self):
        """
        returns a dictionary containing all data
        of a Student instance
        """
        dict = {}
        for attr_name, attr_val in vars(self).items():
            dict.update({attr_name: attr_val})
        return dict
