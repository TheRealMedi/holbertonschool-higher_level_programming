#!/usr/bin/python3
from typing import Counter


def safe_print_list(my_list=[], x=0):
    Counter = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            Counter += 1
        except IndexError:
            break
    print()
    return Counter
