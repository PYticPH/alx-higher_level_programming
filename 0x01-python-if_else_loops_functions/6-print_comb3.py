#!/usr/bin/python3
for unit in range(9):
    for tens in range(unit + 1, 10):
        if (unit == 8) & (tens == 9):
            print("{}{}".format(unit, tens))
        else:
            print("{}{}".format(unit, tens), end=', ')
