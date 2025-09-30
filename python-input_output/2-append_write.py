#!/usr/bin/python3
"""
    Module for appending a string at the end of the text file
    and
    returning the length of characters written
"""


def append_write(filename="", text=""):
    """
    Append a string to a text file and return the length of characters written

    Args:
        filename (str):the path to the file to read(defaults to empty string)

    Return:
        none
    """
    with open(filename, 'a', encoding='utf-8') as f:
        characters_written = f.write(text)

    return characters_written