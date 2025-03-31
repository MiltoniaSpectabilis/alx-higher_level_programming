#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        squared_row = map(lambda x: x ** 2, row)
        print(squared_row)
        result.append(list(squared_row))
    print(result)
