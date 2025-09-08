#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        my_list.sort()
        my_list.reverse()
        max_value = my_list[0]
        return max_value
    return None
