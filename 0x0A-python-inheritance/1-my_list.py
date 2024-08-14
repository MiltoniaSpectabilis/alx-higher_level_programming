#!/usr/bin/python3
"""MyList class."""


class MyList(list):
    """A subclass of list that can print its sorted elements."""

    def print_sorted(self):
        """Print the list, but sorted (ascending sort)."""
        print(sorted(self))
