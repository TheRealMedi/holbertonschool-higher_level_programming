#!/usr/bin/python3
"""
Definning a function wich appends a string.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end.
    Argumments:
        filename (str): The name of the file to write into.
        text     (str): Text to  write into the file.
    Returns:
        Number of the characters added.
    """
    with open(filename, "a", encoding="uff_8") as file:
        return file.write(text)
