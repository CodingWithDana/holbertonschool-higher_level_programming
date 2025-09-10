#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    # Initialise result list (to store division results)
    new_list = []

    for i in range(list_length):
        # Divide the element at index i from both lists
        try:
            result = my_list_1[i] / my_list_2[i]
        # Catch 'wrong type' error
        except TypeError:
            print('wrong type')
            result = 0
        # Catch 'division by zero' error
        except ZeroDivisionError:
            print('division by 0')
            result = 0
        # Catch "out of range" missing index error
        except IndexError:
            print('out of range')
            result = 0
        # Finally block, append the result to the new_list
        finally:
            new_list.append(result)
    # After loop finishes, return new_list
    return new_list
