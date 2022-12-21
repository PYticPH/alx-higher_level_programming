#!/usr/bin/python3

def safe_print_division(a, b):
    # Function to divide two integers and print the result
    result = None
    try:
        result = a / b
        print("Inside result: {}".format(result))
    except ZeroDivisionError:
        print("Inside result: {}".format(result))
    finally:
        return (result)
