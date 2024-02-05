#!/usr/bin/python3
"""Defines an inherited class checking function"""


def inherits_from(obj, a_class):
    """Checks if an object ia an inherited instance of a class

    Args:
        obj: The object to check.
        a_class (type): The class to match the object type to.
    Returns:
        True - If obj is an inherited instance of a class.
        False - Otherwise.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
