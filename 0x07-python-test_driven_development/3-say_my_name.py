#!/usr/bin/python3
"""
Definning a funtion wich print entire name properly.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>.
    Arguments:
        Datatypes.
    Raises:
        TypeError (first_name): first_name must be a string.
        TypeError  (last_name):  last_name must be a string.
    Return:
        ----.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
