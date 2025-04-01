#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")


print_sorted_dictionary(
    {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]})
