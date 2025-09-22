#!/usr/bin/python3
"""
    Writes a function that if the object
    is an instance of a class that inherited (directly or indirectly)
    from the specified class
    otherwise False
"""


def inherits_from(obj, a_class):
    """
        Returns True if obj is an instance of a subclass of a_class,
        otherwise False
    """
    obj_class = type(obj)

    # Exclude this case when obj is EXACTLY an instance of a_class
    if obj_class is a_class:
        return False

    # Traverse through the class hierachy
    for base in obj_class.__mro__:
        if base is a_class:
            return True

    return False
