#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return (False)
    new_list = []
    for num in my_list:
        new_list.append(bool(num % 2 == 0))
    return (new_list)
