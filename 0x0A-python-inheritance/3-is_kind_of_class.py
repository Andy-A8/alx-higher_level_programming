#!/usr/bin/python3
"""Defines a class and an inherited class checking function"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class
    or an inherited instance of a class.

    Args:
        obj: The object to check.
        a_class (type): The class to match the object type to.

    Returns:
        True - If obj is an instance or inheritd instance of a_class.
        False - Otherwise.
    """

    if isinstance(obj, a_class):
        return True
    return False
