#!/usr/bin/python3
""" Module for reading and printing the content of a UTF-8 text file """


def read_file(filename=""):
    """
    Read a text file (UTF8) and print to the stdout

    Args:
        filename (str):the path to the file to read(defaults to empty string)

    Return:
        none
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
