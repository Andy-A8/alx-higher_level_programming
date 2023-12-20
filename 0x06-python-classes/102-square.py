#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a square

        Args:
            size (int): The size of the new square
        """
        #  if and elif statements based on 3-square.py are eliminated
        #  since they are  not required in the question
        self.__size = size

    @property
    def size(self):
        """Get the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)   # or (self.__size ** 2)

    def __eq__(self, other):
        """The == (equal to) comparison to a square"""
        return self.area() == other.area()

    def __neq__(self, other):
        """The != (not equal to) comparison to a square"""
        return self.area() != other.area()

    def __gt__(self, other):
        """The > (greater than) comparison to a square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """The >= (greater than or equal to) comparison to a square"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """The < (less than) comparison to a square"""
        return self.area() < other.area()

    def __le__(self, other):
        """The <= (less than or equal to) comparison to a square"""
        return self.area() <= other.area()
