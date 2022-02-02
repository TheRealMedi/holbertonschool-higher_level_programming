#!/usr/bin/python3
"""
Definning a function wich appends a string.
"""
import json


def to_json_string(my_obj):
    """
    Returns a JSON Rep of a string obj.
    """
    return json.dumps(my_obj)
