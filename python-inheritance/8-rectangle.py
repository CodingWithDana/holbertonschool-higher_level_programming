#!/usr/bin/python3
""" Defines a class BaseGeometry """


class BaseGeometry:
    """ A base class for geometry objects """

    def area(self):
        """ Public instance method to raise a custom Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Public instance method to validate value

            Args:
            name (str): name of the parameter (used in error message)
            value (int): value to validate
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

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
