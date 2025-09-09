#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_a_dictionary = []
    for value in a_dictionary.values():
        new_a_dictionary = value * 2
    return new_a_dictionary
