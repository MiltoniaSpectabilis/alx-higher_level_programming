#!/usr/bin/python3

def no_c(my_string):
    my_string_no_c = []
    for char in my_string:
        if char not in 'cC':
            my_string_no_c.append(char)
    return ''.join(my_string_no_c)
