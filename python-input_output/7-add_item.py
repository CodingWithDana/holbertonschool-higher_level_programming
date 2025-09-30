#!/usr/bin/python3
"""
    Script for adding all command-line arguments to a Python list
    and saves them to a JSON file
"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing lists from the json file,
# otherwise create an empty list if the file doesn't exist
try:
    lists = load_from_json_file(filename)
except FileNotFoundError:
    lists = []

# Add all command-line arguments (excluding the script name)
lists.extend(sys.argv[1:])

# Save the updated list back to the JSON file
save_to_json_file(lists, filename)
