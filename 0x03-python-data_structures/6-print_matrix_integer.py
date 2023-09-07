#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if len(i) != 0:
            print("{:d} {:d} {:d}".format(*i))
