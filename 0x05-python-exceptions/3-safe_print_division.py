#!/usr/bin/python3
from unittest import result


def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result), end="")
        print()
    return result
