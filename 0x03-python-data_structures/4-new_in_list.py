#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    magic_counter = len(my_list)
    if idx < 0 or idx > magic_counter - 1:
        return my_list
    new_list = [None] * magic_counter
    for i in range(0, magic_counter):
        if i == idx:
            new_list[i] = element
        else:
            new_list[i] = my_list[i]
    return new_list
