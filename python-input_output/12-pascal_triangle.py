#!/usr/bin/python3
"""
    Module for returning a list of lists of integers
    representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
        Return a list of lists representing Pascal's Triangle of n

        Args:
            n (int): number of rows

        Return:
            list: list of lists of integers
    """

    # Check: empty list
    if n <= 0:
        return []

    # First row
    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        # Each row starts and ends with 1
        row = [1]
        # Compute middle values
        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
