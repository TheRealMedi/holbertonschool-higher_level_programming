#!/usr/bin/python3
"""Empty class wich defines a square."""


class Square:
    """Representation of Square class."""

    def __init__(self, size=0):
        """Initializing Square
        """
        self.__size = size

    def area(self):
        """Public instance wich returns the area."""
        return(self.__size * self.__size)

    @property
    def size(self):
        """returns the size."""
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
