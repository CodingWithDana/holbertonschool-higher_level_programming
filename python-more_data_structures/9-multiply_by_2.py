#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_a_dictionary = {}
    for key, value in a_dictionary.items():
        new_a_dictionary[key] = value * 2
    return new_a_dictionary
