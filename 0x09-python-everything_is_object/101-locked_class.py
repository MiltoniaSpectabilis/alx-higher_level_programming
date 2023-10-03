#!/usr/bin/python3


'''locked class module'''


class LockedClass:

    """
    Class that prevents new
    instances using the variable
    __slots__
    """
    __slots__ = "first_name",
