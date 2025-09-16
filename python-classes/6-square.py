#!/usr/bin/python3
""" Module for the Square class """


class Square:
    """
    A class that defines a square with size and position

    Attributes:
        __size (int): size of the square (private)
        __position(tuple): position of the square (private)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise the square

        Args:
            size (int): the size of the square (defaults to 0)
            position (tuple): position of the square (default (0, 0))

        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
            TypeError: if position is not a tuple of 2 positive integers
        """
        # Use the property setters for validation
        self.size = size
        self.position = position

    # define getter method to access private attribute 'size'
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

    # define getter method to access private attribute 'position'
    @property
    def position(self):
        """
        Get the position of the square
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        """ Set the position of the square with explicit validation """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        
        self.__position = value

    # Add public instance method area()
    def area(self):
        """
        Return the current square area

        Returns:
            int: area of the square
        """
        return self.__size * self.__size

    # Add public instance method my_print()
    def my_print(self):
        """
        Print the square using #

        If size is 0, print an empty line
        """
        if self.__size == 0:
            print()
        
        # print vertical 
        for _ in range(self.__position[1]):
            print()
            
        for _ in range(self._size):
            # print horizontal 
            print(" " * self.__position[0], end="")
            # print square row
            print("#" * self._size)
