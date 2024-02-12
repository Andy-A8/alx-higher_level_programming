#!/usr/bin/python3
"""Defines a class Base."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries
         Args:
            list_dictionaries (list): A list of dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
