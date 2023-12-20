#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size):
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
        """Rturn the current area of the square"""
        return (self.__size * self.__size)   # or (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")

        if self.__size == 0:
            print("")
