#!/usr/bin/python3
"""
Definning a funtion wich print entire name properly.
"""


def print_square(size):
    """
    Arguments:
    Raises:
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

    