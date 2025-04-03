#!/usr/bin/python3

def roman_to_int(roman_string):

    roman_numerals = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100,
                      'D': 500, 'M': 1000}

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    sum_numerals = 0
    prev_value = 0

    for char in reversed(roman_string):
        if char not in roman_numerals:
            return 0
        curr_value = roman_numerals[char]

        if curr_value >= prev_value:
            sum_numerals += curr_value
        else:
            sum_numerals -= curr_value
        prev_value = curr_value

    return sum_numerals
