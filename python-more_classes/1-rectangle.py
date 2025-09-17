#!/usr/bin/python3
""" Nameless module for the Rectangle class """


class Rectangle:
    """A rectangle by width and height"""

    def __init__(self, width=0, height=0):
        """
        Initialise the rectangle

        Args:
            width (int): the width of the rectangle (default 0)
            height (int): the height of the rectangle (default 0)
        """
        # triggers width setter
        self.width = width
        # triggers height setter
        self.height = height

    @property
    def width(self):
        """Retrieve/get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation

        Args:
            value (int): the new width of the rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        # triggers the setter to assign new value to width attribute
        self.__width = value

    @property
    def height(self):
        """Retrieve/get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation

        Args:
            value (int): new height of the rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
