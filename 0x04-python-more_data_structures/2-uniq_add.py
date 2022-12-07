#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return (my_list)
    sum = 0
    for num in set(my_list):
        sum += num
    return (sum)
