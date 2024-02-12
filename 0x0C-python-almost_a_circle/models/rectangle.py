#!/usr/bin/python3
"""Defines a class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height <= 0.
            TypeError: If either x or y is not an integer.
            ValueError: If either x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

# Getter and Setter functions of attributes except id
    @property
    def width(self):
        """Get the width of the Rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the value for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set the value for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinates of the Rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """set the value for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinates of the Rectangle"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """set the value for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Defines the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Prints the Rectangle instance with the # character"""
        for y in range(self.__y):
            print("")
        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Returns the print() and str() representation of the Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args):
        """Assigns an argument to each attribute
            Args:
            *args (int): New attribute values.
                1st argument - represents id attribute
                2nd argument - represents width attribute
                3rd argument - represents height attribute
                4th argument - represents x attribute
                5th argument - represents y attribute
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
