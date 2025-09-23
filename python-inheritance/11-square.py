#!/usr/bin/python3
""" Defines BaseGeometry and Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ Initialise the Square with size """
        # validate size using integer_validator from BaseGeometry (inherited)
        self.integer_validator("size", size)
        self.__size = size
        # initialise the Rectangle part (width and height both equal size)
        super().__init__(size, size)

    def area(self):
        """ Return area of the Square """
        return self.__size ** 2

    def __str__(self):
        """ Return the string representation of the Square """
        return "[Square] {}/{}".format(self.__size, self.__size)
