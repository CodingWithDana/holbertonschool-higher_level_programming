#!/usr/bin/python3
"""
    Module for returning the dictionary description
    with simple data structures (list, dictionary, string,
    integer, and boolean) of a class instance
"""


def class_to_json(obj):
    """
        Return the dictionary description with simple data structures (list,
        dictionary, string,integer, and boolean) of a class instance

        Args:
            dict: Dictionary of the object's attributes
    """
    return obj.__dict__
