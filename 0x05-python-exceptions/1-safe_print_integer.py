#!/usr/bin/python3
from ast import Try


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False