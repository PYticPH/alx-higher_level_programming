#!/usr/bin/python3
def print_last_digit(number):
    sign = 1
    if number < 0:
        sign = -1
    lastNum = (number * sign) % 10
    print("{}".format(lastNum), end='')
    return lastNum
