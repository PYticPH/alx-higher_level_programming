#!/usr/bin/python3
""" A class Square  """


class Square:
    """ clas square """
    def __init__(self, size=0, position=(0, 0)):
        """ initialize private attributes """
        self.size = size
        self.position = position

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
        for i in range(0, self.__position[1]):
            print()
        if self.__size:
            for i in range(0, self.__size):
                print("{}{}".format(
                    ' ' * self.__position[0], '#' * self.__size))
        else:
            print()

    @property
    def position(self):
        """ get the value of position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ set the value of position """
        if (not isinstance(value, tuple)) | (value is None):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not len(value) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(value[0], int)) | (not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0) | (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
