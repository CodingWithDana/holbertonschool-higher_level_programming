#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    # Divide two integer
    try:
        result = a / b
    # Catch division by zero
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
