#!/usr/bin/python3
"""Defines a python class to JSON function."""


def class_to_json(obj):
    """Returns the dictionary of a simple data structure"""
    return obj.__dict__
