#!/usr/bin/python3
def roman_to_int(roman_string):
    # Return 0 if input is not a string
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    # Mapping of Roman numerals to integers:
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    # Keep track of the final integer value of the Roman numeral
    total = 0
    prev_value = 0

    # Loop through the Roman numeral from right to left
    for char in reversed(roman_string):
        if char not in roman_map:
            # Invalid character found
            return 0
        value = roman_map[char]

        if value < prev_value:
            # Minus smaller value
            total = total - value
        else:
            # Add larger or equal value
            total = total + value

        prev_value = value
    return total
