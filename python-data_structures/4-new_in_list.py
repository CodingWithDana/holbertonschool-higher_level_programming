#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Make a copy of my_list
    new_list = my_list.copy()
    
    # Check if index is valid
    if 0 <= idx <= len(my_list):
    # Replace the element at a given index
        new_list[idx] = element
    
    return new_list
