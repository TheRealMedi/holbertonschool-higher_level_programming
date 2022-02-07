#!/usr/bin/python3
"""
Definning a Base Model class.
"""

class Base:
    """
    Represents the Base model.
    Argumments:
        __nb_objects (int): Is the number of instancied Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing a New Base.
        Argumments:
            id (int): Identity of the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        