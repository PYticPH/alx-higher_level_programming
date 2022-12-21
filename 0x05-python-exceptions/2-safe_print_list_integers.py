#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ''' Function to print the first x elements of
    a list(integer only)'''
    num = 0
    count = 0
    for num in range(1, x + 1):
        try:
            print("{:d}".format(my_list[num - 1]), end='')
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return (count)
