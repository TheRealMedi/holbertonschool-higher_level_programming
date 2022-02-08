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
            height (int): The heigth of the new Rectangle.
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

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getting the height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getting the x coordinate of the Rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getting the Y coordinate of the Rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returning the Recttangle's Area.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print a Rectanlge with '#' character.
        """
        print("\n" * self.y, end='')
        for i in range(self.height):
            print(" " * self.x, end='')
            print("#" * self.width)

    def __str__(self):
        """"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
