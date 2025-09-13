#!/usr/bin/python3
"""
This module docstring provides a function to
print a square with the character '#'

print_square function validates the input,
then prints a square with the character '#'
"""


def print_square(size):
    """
    Prints a square with the character '#'

    Args:
        size (int): The size length of the square
    Returns:
        A square of hashes
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for _ in range(size):
        print("#" * size)
