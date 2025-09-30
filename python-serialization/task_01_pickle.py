#!/usr/bin/python3
"""
    Module for serialising and deserialising custom Python objects
    using pickle module
"""


import pickle


class CustomObject:
    """ A custom object class representing a student's details """
    
    def __init__(self, name: str, age: int, is_student: bool):
        """
            Initialise a CustomObject instance

            Args:
                name (str): name of the student
                age (int): age of the student
                is_student (bool): student status
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
            Serialize the current instance of the object and
            save it to the provided filename

            Args:
                filename (str): the file to save the serialised object
                
            Return: None
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            return True
        except Exception:
            return None

        @classmethod
        def deserialize(cls, filename):
            """
                Deserialize an object from a file and 
                return an instance of the CustomObject from the provided name

                Args:
                    filename (str): the file containing the serialised object

                Return:
                    CustomObject: the deserialised object
                    otherwise None if an error occurred
            """
            try:
                with open(filename, 'rb') as f:
                    return pickle.load(f)
            except Exception:
                return None

    def display(self):
        """
            Print the object's attributes in a formatted way
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
