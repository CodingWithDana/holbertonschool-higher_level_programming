#!/usr/bin/python3
""" 
    Module for writing a string to a text file and 
    returning the length of characters written 
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file and return the length of characters written

    Args:
        filename (str):the path to the file to read(defaults to empty string)

    Return:
        none
    """
    with open(filename, 'w', encoding='utf-8') as f:
        characters_written = f.write(text)

    return characters_written
