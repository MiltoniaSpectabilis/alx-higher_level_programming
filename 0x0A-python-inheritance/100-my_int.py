#!/usr/bin/python3
"""MyInt class."""


class MyInt(int):
    """A subclass of int that inverts the == and != operators."""

    def __eq__(self, other):
        """Return the opposite of the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return the opposite of the != operator."""
        return super().__eq__(other)
