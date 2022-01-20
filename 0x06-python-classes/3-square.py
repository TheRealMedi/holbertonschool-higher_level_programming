#!/usr/bin/python3
"""Empty class wich defines a square."""


class Square:
    """Representation of square class"""

    def __init__(self, size=0):
        """Intializing new square
        """
        if type(size, int) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size
