#!/usr/bin/python3
"""Define a class Rectangle that inherits from  BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeeometry"""

    def __init__(self, width, height):
        """Initialize a new rectangle

        Args:
            width (int): The width of the new rectanlge.
            height (int): The height of the new rectangle.
        """

        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = heigh
