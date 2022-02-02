#!/usr/bin/python3
"""
Definning a function which writes into a JSON file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    write an object into a json text file.
    """
    with open(filename, "w") as file:
        return json.dump(my_obj, file)
