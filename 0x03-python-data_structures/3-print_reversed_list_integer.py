#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    rev_list = list(reversed(my_list))
    for i in range(len(rev_list)):
        print("{:d}".format(rev_list[i]))
