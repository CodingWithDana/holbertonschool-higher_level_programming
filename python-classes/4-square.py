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

        """
        # Use the property setter for validation
        self.size = size
  
    @property
    def size(self):
        """
        Get the size of the square
        
        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation

        Args:
            value (int): new size of the square
        
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # Add public instance method area()
    def area(self):
        """
        Return the current square area

        Returns:
            int: area of the square
        """
        return self.__size * self.__size
