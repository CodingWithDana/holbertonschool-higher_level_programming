#!/usr/bin/python3
"""
        Defines a Student class including their:
        first name, last name and age
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """ Instantiate the public instance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ 
            Retrieve a dictionary representation of the Student instance

            If the "attrs" is a list of strings, only attributes with names
            contained in this list are returned. 

            Otherwise, return all attributes.

            Args:
                attrs (list): List of attribute names to retrieve

            Return:
                dict: Dictionary of the attribute names in the list only
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            # Include only selected attributes that exist in the object (list)
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

            # Otherwise return all attributes
            return self.__dict__.copy()
