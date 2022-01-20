#!/usr/bin/python3
"""Empty class wich defines a square."""


class Square:
    """Representation of Square class."""

    def __init__(self, size=8):
        """Initializing Square.
        """
        self.size = size

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

    def my_print(self):
        """Print the square."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
