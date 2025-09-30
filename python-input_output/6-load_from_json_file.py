#!/usr/bin/python3
"""
    Module for creating an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Create an Object from a “JSON file”
    """
    with open(filename, "w", encoding="utf-8") as filename:
        return json.load(filename)
