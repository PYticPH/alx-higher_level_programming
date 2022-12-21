#!/usr/bin/python3
from os import write


def safe_print_integer_err(value):
    # Function to print an integer
    m = "Exception: Unknown format code 'd' for object of type 'str'\n"
    try:
        print("{:d}".format(value))
    except ValueError:
        write(2, m.encode("UTF-8"))
        return (False)
    return (True)
