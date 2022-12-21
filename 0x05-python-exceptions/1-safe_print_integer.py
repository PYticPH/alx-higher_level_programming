#!/usr/bin/python3

def safe_print_integer(value):
    # funcion to print integer value only
    try:
        print("{:d}".format(value))
    except ValueError:
        return (False)
    return (True)
