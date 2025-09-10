#!/usr/bin/python3
"""
This module docstring provides a function to add two integers safely.

If the inputs are integers or floats, then cast floats to integers,
and raise appropriate errors if the inputs are invalid.
"""

def add_integer(a, b=98):
    """
    Adds two integers after validating and casting the inputs.

    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number to be added, defaults to 98.

    Raises:
        TypeError: If either 'a' or 'b' is not an integer or float.

    Returns:
        int: The sum of 'a' or 'b', both casted to integers if necessary.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
