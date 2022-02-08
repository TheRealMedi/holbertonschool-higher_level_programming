#!/usr/bin/python3
"""
Definning a Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Representing a Square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializing a new Square.

        Argumments:
            size (int): Size of Square.
            x    (int): X Square's coordinate.
            y    (int): Y Square's coordinate.
            id   (int): Square's identify.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getting Square's size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setting Square's size.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a Standard print().
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
