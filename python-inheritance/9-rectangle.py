#!/usr/bin/python3
""" Defines BaseGeometry and Rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Define new class Rectangle that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Initialise a rectangle with width and height """
        # Validate width and height using BaseGeometry method
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Private attributes
        self.__width = width
        self.__height = height

    def area(self):
        """ Return the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Return the string representation of the rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
