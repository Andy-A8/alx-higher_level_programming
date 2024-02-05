#!/usr/bin/python3
"""Defines a function that adds a new attribute to an object"""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if its possible

    Args:
        obj: The object to which the attribute is added.
        att: The attribute name.
        value: The value to be set for the attribute.

    Raises:
        TypeError: If the attribute cannot be added.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
