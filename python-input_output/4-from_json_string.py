#!/usr/bin/python3
"""
    Module for returning an object
    (Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Returning the JSON representation of an object (string)
    """
    return json.loads(my_str)
