#!/usr/bin/python3
"""
Definning a file reading function.
"""


from encodings import utf_8
from fileinput import filename


def read_file(filename=""):
    """
    Prints the UTF8 file to stdout.
    """
    with open(filename, encoding="utf_8") as file:
        print(file.read(), end="")
