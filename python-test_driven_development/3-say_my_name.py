#!/usr/bin/python3
"""
This module docstring provides a function to
print My name is <first name> <last name>

say_my_name function validates the input,
then prints each element accordingly
"""


def say_my_name(first_name, last_name=""):
    """
    Print the first name and last name

    Args:
        first_name (str): the first name
        last_name (str): the last name. Defaults to ""

    Returns:
        a string with the first name and last name
  
    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
