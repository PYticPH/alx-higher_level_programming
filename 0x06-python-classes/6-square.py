#!/usr/bin/python3
"""
class Square that defines a square by: (based on 5-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the
message size must be an integer
if size is less than 0, raise a ValueError exception with the message
size must be >= 0
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers, otherwise raise a TypeError
exception with the message position must be a tuple of 2 positive integers
Instantiation with optional size and optional position:
def __init__(self, size=0, position=(0, 0)): Public instance method:
def area(self): that returns the current square area Public instance method:
def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
"""


class Square:
    """ clas square """
    def __init__(self, size=0, position=(0, 0)):
        """ initialize private attribute size """
        self.__size = size
        self.__position = position

    def area(self):
        """ return the current square area """
        return (self.__size * self.__size)

    @property
    def size(self):
        """ retrieve the value of size """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ set value of size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ print square with '#' character """
        if self.__size:
            if self.__position[1]:
                print("{}".format(''))
            for i in range(0, self.__size):
                print("{}{}".format(
                    ' ' * self.__position[0], '#' * self.__size))
        else:
            print()

    @property
    def position(self):
        """ return the value of position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ set the value of position """
        if not isinstance(value, type((0, 0))) | len(value) != 2:
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) & isinstance(value[1], int)):
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        if value[0] < 0 | value[1] < 0:
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        else:
            self.__position = value
