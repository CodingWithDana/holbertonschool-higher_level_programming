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

    def to_json(self):
        """ Retrieve a dictionary representation of the Student instance """
        return self.__dict__
