#!/usr/bin/python3
"""
This module docstring provides a function to add two integers after validating their types.

If the inputs are integers or floats, then cast floats to integers,
and raise appropriate errors if the inputs are invalid.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats after converting them to integers.
    
    Both a and b must be integers or floats, otherwise a TypeError is raised.
    Floats are truncated to integers before addition.
    Returns the sum of a and b as an integer.
    """
    # a is not int and a is not float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    # b is not int and b is not float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
