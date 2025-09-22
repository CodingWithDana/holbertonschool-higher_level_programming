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
        if not isinstance (value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
