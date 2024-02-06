#!/usr/bin/python3
"""Defines a file appending function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)

    Args:
        filename (str): The name of the file to be appended upon.
        text (str): The string to append to the file.

    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
