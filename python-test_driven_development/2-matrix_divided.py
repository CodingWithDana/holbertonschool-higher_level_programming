#!/usr/bin/python3
"""
This module docstring provides a function to divide all
elements of a matrix by a given divisor

matrix_divided function validates the input,
then divides each element by the given divisor
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix

    Args:
        matrix: list of lists of integers/floats
        div: number (int or float) to divide by

    Returns:
        A new matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: if matrix is not a list of lists of numbers,
            or if rows are not the same size,
            or if div is not a number.
        ZeroDivisionError: for div=0
    """
    # Check matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Check matrix is not empty
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Check each row is a list
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Check each element is int or float
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Check row size consistency
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # Check div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
