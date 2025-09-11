#!/usr/bin/python3
def best_score(a_dictionary):
    # If the dictionary is empty
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    # Initialise the variables to track the best key and its value
    best_key = None
    best_value = None

    # Loop through each key-value pair in a_dictionary
    for key, value in a_dictionary.items():
        if best_value is None or value > best_value:
            best_value = value
            best_key = key
    # Return the key with the best value
    return best_key
