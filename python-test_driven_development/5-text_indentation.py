#!/usr/bin/python3
"""
This module docstring provides a function to
prints a text with 2 new lines after each of
these characters: ., ? and :

text_indentation function validates the input,
then prints a text with 2 new lines after specified characters
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text
    Returns:
        A text with 2 new lines after each of these characters: ., ? and :

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        char = text[i]
        print(char, end="")
        if char in ".?:":
            print("\n")
            # Skip the space after character
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
