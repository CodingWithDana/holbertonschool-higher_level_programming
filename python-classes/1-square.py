#!/usr/bin/python3
""" Module for the Square class """


class Square:
    """
    A class that defines a square

    Attributes:
        __size (int): size of the square (private)
    """

    def __init__(self, size):
        """
        Initialise the square
        
        Args:
            size: the size of the square (no type/value verification)
        """
        self.__size = size
