#!/usr/bin/python3

"""Module that contains functions for matrix operations"""


def matrix_divided(matrix, div):
    """divides matrix by scalar integer, rounded to two decimal places"""
    import decimal
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_msg)
    len_rows = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        len_rows.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
