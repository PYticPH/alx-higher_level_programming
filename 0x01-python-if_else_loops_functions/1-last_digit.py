#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1
if number < 0:
    sign = -1
lastNum = (number * sign) % 10
if lastNum * sign > 5:
    print(f"Last digit of {number} is {lastNum * sign} and is greater than 5")
elif lastNum * sign == 0:
    print(f"Last digit of {number} is {lastNum * sign} and is 0")
else:
    print(f"Last digit of {number}", end=" ")
    print(f"is {lastNum * sign} and is less than 6 and not 0")
