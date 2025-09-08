#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Return a new list of booleans indicating whether each number is divisible by 2
    new_list = []
    for num in my_list:
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
