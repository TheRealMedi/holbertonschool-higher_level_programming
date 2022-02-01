#!/usr/bin/python3
"""
Definnin a function which
writes a text into a UTF8 FILE.
"""


def write_file(filename="", text=""):
    """
    Write a string into a UTF8 File.
    Arguments:
        filename (str): Name of the file to write into.
        text     (str): Text to write into the file.
    Returns:
        number of the char written.
    """
    with open(filename, "w", encoding="utf_8") as file:
        return file.write(text)
