#!/usr/bin/python3

def uniq_add(my_list=[]):
    no_dupes = set(my_list)
    sum = 0
    for i in no_dupes:
        sum += i
    return sum
