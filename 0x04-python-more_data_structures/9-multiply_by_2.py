#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    squared = {k: v * 2 for k, v in a_dictionary.items()}
    return squared
