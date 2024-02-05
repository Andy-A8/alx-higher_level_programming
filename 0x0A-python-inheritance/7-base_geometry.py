#!/usr/bin/python3
"""Define a class BaseGeometry"""


class BaseGeometry:
    """Represents base geometry"""

    def area(self):
        """Method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an integer

        Args:
            name (str): The name of the value
            value (int): The value to validate.

        Raises:
            TypeError: If value is an integer.
            ValueError: If value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError(name + "must be an integer")
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
