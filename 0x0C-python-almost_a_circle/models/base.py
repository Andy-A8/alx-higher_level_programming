#!/usr/bin/python3
"""Defines a class Base."""


class Base:
    """Represents the base of this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base

        Args:
            id (int): The identity of the new Base.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
