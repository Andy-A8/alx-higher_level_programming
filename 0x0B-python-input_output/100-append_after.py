#!/usr/bin/python3
"""Defines a text to file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file,
        after each line containing a specific string

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in the file.
        new_string (str): The string to be inserted.
    """

    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
