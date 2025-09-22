#!/usr/bin/python3
""" Defines a class BaseGeometry """


class BaseGeometry:
    """ A base class for geometry objects """
    def area(self):
        """ Public instance method to raise a custom Exception """
        raise Exception("area() is not implemented")
