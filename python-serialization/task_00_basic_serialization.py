#!/usr/bin/python3
"""
    Module for adding the functionality to serialize a Python dictionary to a JSON file and
    deserialize the JSON file to recreate the Python Dictionary
"""
import json


def serialize_and_save_to_file(data, filename):
    """
        Serialize Python dictionary to a JSON file

        Args:
            data: A Python Dictionary with data
            filename: The filename of the output JSON file.
                    If the output file already exists,
                    it should be replaced

        Return: None (because this function just writes to a file)
    """
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """
        Deserialise JSON from file back into a dictionary

        Args:
            filename: filename of the input JSON file

        Return:
            dict: The deserialised data from the JSON file.
    """
    with open(filename, "r") as f:
        return json.load(f)
