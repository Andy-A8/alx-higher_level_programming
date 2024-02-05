#!/usr/bin/python3
"""Defines a specified class checking function"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.


    Args:
        obj: The object to check.
        a_class (type): The class to match the object type to.
    Returns:
        True - If obj is exactly an instance of the specified class.
        False - Otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
