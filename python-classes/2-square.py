#!/usr/bin/python3
""" Module for the Square class """


class Square:
    """
    A class that defines a square

    Attributes:
        __size (int): size of the square (private)
    """

    def __init__(self, size=0):
        """
        Initialise the square

        Args:
            size: the size of the square (defaults to 0)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        # Validating the 'size'
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        # Assigning the value to the private instance attribute 'size'
        self.__size = size
