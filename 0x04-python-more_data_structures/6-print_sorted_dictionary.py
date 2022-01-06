#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = a_dictionary
    for keys, values in sorted(sorted_dictionary.items()):
        print("{:s}: {}".format(keys, values))
