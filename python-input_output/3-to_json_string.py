#!/usr/bin/python3
"""
    Module for returning the JSON representation of 
    an object (string)
"""

import json
def to_json_string(my_obj):
    """
    Returning the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
