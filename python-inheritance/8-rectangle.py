#!/usr/bin/python3
""" Defines BaseGeometry and Rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Define new class Rectangle that inherits from BaseGeometry """


    def __init__(self, width, height):
        """ Initialise a rectangle with width and height """
        # Validate width and height using BaseGeometry method: integer_validator
        self.integer_validator("width", width)
        self.integer_validator("height", height)
    
        # Private attributes
        self.__width = width
        self.__height = height
