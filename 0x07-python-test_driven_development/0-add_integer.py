#!/usr/bin/python3
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """Returns the integer addition of a and b.

    Float arguments are typecasted to integers before addition is done.

    Raises:
        TypeError: If either a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
