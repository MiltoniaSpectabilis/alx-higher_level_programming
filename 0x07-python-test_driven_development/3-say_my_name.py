#!/usr/bin/python3
"""
A simple module that prints
'My name is <first_name> <last_name'
"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints
    'My name is <first_name> <last_name>'
    """
    # if not last_name and isinstance(first_name, str):
    #     print(f"My name is {first_name}")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
