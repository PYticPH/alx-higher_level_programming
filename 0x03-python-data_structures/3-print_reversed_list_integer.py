#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) < 1:
        return (None)
    my_list.reverse()
    for idx in my_list:
        print("{:d}".format(idx))
