#!/usr/bin/python3
"""
    Defines the lookup function that returns all attributes
    and methods of an object
"""


def lookup(obj):
    """ Return a list of all available attributes and methods of obj """
    # dir() already returns a list
    return dir(obj)
