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

    def update(self, *args, **kwargs):
        """
        Square's update class.

        Argumments:
             *args   (ints): New attribute values.
                1st arg: means id attribute.
                2nd arg: means size attribute.
                3rd arg: means x coordinate atribute.
                4th arg: means y coordinate attribute.
            **kwargs (dict): Key/Value pair of attributes.
        """
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                    self.height = args[i]
                if 1 == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """
        Return a Standard print().
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
