#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for idx in my_list:
        if idx < 0 or idx > len(my_list):
            return None
        else:
            return my_list[idx]
