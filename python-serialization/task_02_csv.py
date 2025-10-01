#!/usr/bin/python3
"""
    Module for converting a CSV file to JSON
    and save as data.json
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON and save it as data.json

    Args:
        csv_filename (str): the path to the CSV file

    Return:
        bool: True if successful, otherwise False
    """
    try:
        # read CSV file
        with open(csv_filename, mode ='r', newline='',
                  encoding='utf-8') as csvfile:
            formatted_data = list(csv.DictReader(csvfile))

        # write JSON data to file
        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(formatted_data, jsonfile)
    except FileNotFoundError:
        return False

    return True

# #TEST MY CODE:
# csv_file = "data.csv"
# convert_csv_to_json(csv_file)
# print(f"Data from {csv_file} has been converted to data.json")