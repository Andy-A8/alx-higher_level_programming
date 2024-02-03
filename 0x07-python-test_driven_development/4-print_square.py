#!/usr/bin/python3
"""Defines a square printing function"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): The height/wedth of the square.

    Raises:
        TypeError: If the size is not an integer.
        TypeError: If the size is a float and less than zero.
        ValueError: If size < 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print('#', end="") for j in range(size)]
        print("")
