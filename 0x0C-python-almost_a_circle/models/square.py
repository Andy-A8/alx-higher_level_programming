#!/usr/bin/python3
"""Defines a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a new square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new square

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Squaree.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the print() and str() representation of the the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Get the size of the Square"""
        return (self.width)

    @size.setter
    def size(self, value):
        """set the value for size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
