#!/usr/bin/python3
"""Empty class wich defines a square."""


class Square:
    """Representation of Square class."""

    def __init__(self, size=0):
        """Initializing Square.
        """
        if type(size) is not int:
                raise TypeError("size must be an integer")
        if size < 0:
                raise ValueError("size must be >= 0")
        self.size=size
