#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = tuple_a[:2] + (0, 0)
    tuple_b = tuple_b[:2] + (0, 0)

    a_1, a_2 = tuple_a[:2]
    b_1, b_2 = tuple_b[:2]

    tuple_c = (a_1 + b_1, a_2 + b_2)

    return tuple_c
