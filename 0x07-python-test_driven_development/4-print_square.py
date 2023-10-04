#!/usr/bin/python3

"""Module that contains functions for text indentation"""


def text_indentation(text):
    """Print a text with 2 new lines after each '.', '?', and ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special_chars = ['.', '?', ':']
    new_text = ''
    for char in text:
        new_text += char
        if char in special_chars:
            new_text += '\n\n'
    print(new_text.strip())
