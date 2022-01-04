#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    size = len(my_string)
    for i in range(0, size):
        if my_string[i] != "c" and my_string[i] != "c":
            new_string += my_string[i]
    return new_string
