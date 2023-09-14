#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    values_list = list(a_dictionary.values())
    max_value = max(values_list)
    for key, value in a_dictionary.items():
        if value == max_value:
            return key
