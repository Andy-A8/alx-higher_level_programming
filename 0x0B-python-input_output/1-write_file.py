#!/usr/bin/python3
"""Defines a text writing  and line-counting function"""


def write_file(filename="", text=""):
    """Returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
