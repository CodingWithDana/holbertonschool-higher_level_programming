#!/usr/bin/python3
""" Nameless module for the Rectangle class """


class Rectangle:
    """A rectangle by width and height"""

    # public class attribute
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialise the rectangle with optional width and height

        Args:
            width (int): the width of the rectangle (default 0)
            height (int): the height of the rectangle (default 0)
        """
        # triggers width setter
        self.width = width
        # triggers height setter
        self.height = height
        # increment the class attribute for each new instance
        Rectangle.number_of_instances += 1

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

    # Add public instance method to calc rectangle area
    def area(self):
        """ Return the rectangle area"""
        return self.__width * self.__height

    # Add public instance method to calc rectangle perimeter
    def perimeter(self):
        """ Return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ Return the printable representation of the rectangle with # """
        if self.width == 0 or self.height == 0:
            # empty string
            return ""
        # build one row of #
        row = "#" * self.width
        # repeat it for height rows, separated by new lines
        return "\n".join([row for _ in range(self.height)])

    def __repr__(self):
        """ Return a string that can recreate the rectangle with eval() """
        return "Rectangle({}, {})".format(self.width, self.height)
        # or you can use f-string way:
        # return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ Destroy the instance of Rectangle and decrement the number_of_instances """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
