#!/usr/bin/python3

def safe_print_integer(value):
    # funcion to print integer value only
    try:
        print("{:d}".format(value))
    except as is_int:
        is_int = False
        return (is_int)
    return (True)
