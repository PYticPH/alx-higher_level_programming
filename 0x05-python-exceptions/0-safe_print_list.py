#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # function to print x number of elements in a list
    num = 0
    for num in range(1, x + 1):
        try:
            print(my_list[num - 1], end='')
        except IndexError:
            num -= 1
            break
    print()
    return (num)
