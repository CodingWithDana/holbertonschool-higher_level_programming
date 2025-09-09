#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Find the differences (in set_1 not in set_2)
    diff_1 = set(set_1) - set(set_2)
    # Find the differences (in set_2 not in set_1)
    diff_2 = set(set_2) - set(set_1)
    # Combine the differences
    result = sorted(diff_1 | diff_2)
    print(result)
