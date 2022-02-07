#!/usr/bin/python3
"""
Definning a Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Representing a Rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializing a new Rectangle.

        Argumments:
            width  (int): The width of the new Rectangle.
            heigth (int): The heigth of the new Rectangle.
            x      (int): The x coordinate of the new Rectangle.
            y      (int): The Y coordinate of the new Rectangle.
            id     (int): The identify of the new Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getting the width of the Rectangle.
        """
        return self.__width

    @property
    def heigth(self):
        """
        Getting the height of the Rectangle.
        """
        return self.__height

    @property
    def x(self):
        """
        Getting the x coordinate of the Rectangle.
        """
        return self.__x

    @property
    def y(self):
        """
        Getting the Y coordinate of the Rectangle.
        """
        return self.y
