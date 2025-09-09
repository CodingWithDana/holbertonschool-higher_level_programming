#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        for number in row:
            new_row = number ** 2
            new_matrix.append(new_row)
    return new_matrix
