#!/usr/bin/python3
"""Defines a class -MyList- inherited from a list"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        print(sorted(self))
