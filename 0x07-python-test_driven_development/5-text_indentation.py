#!/usr/bin/python3
"""A module that prints a text with two new lines after specific chars"""


def text_indentation(text):
    """
    a function that prints a str with two new lines
    after the following chars:
    ':' '.' '?'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in '?.:':
            print("\n")
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
