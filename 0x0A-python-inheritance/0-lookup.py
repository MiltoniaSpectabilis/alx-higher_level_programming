#!/usr/bin/python3
"""a module that returns the list of available attrs and meths of an obj"""


def lookup(obj):
    """returns the list of available attrs and methds of an obj"""
    return dir(obj)
