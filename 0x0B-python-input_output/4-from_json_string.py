#!/usr/bin/python3
"""Defines a JSON to object function."""
import json


def from_json_string(my_obj):
    """Returns the Python object representation of JSON string"""
    return json.loads(my_obj)
