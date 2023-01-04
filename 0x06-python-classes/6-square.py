#!/usr/bin/python3
""" class Square """


class Square:
    """ clas square """
    def __init__(self, size=0, position=(0, 0)):
        """ initialize private attribute size """
        self.__size = size
        self.position = position

    def area(self):
        """ return the current square area """
        return (self.size * self.size)

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
        if self.size:
            if self.position[1]:
                print("{}".format('' * self.position[1]))
            for i in range(0, self.size):
                print("{}{}".format(
                    ' ' * self.position[0], '#' * self.size))
        else:
            print()

    @property
    def position(self):
        """ return the value of position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ set the value of position """
        if (type(value) is not tuple) | (len(value) != 2):
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        elif (value[0] is not int) | (value[1] is not int):
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        elif (value[0] < 0) | (value[1] < 0):
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        else:
            self.__position = value
