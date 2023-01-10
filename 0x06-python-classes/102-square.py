#!/usr/bin/python3
""" A class Square that defines a square by
- Private atttribute: size
  property def size(self) to retrieve it
  property setter def size(self, value) to set it
- Instantiation with optional size: def __init__(self, size=0)
  size must be an integer, otherwise raise TypeError exception
  with message "size must be an integer"
  if size is less than 0, raise a ValueError exception message
  "size must be >= 0"
- Public instance method def area(self) that returns the current
  square area
"""


class Square:
    """ clas square """
    def __init__(self, size=0):
        """ initialize private attribute size """
        self.__size = size

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

    def __lt__(self, other):
        """ rep. of less than < object"""
        if (not isinstance(other, Square)):
            return NotImplemented
        return (self.size < other.size)

    def __le__(self, other):
        """ rep. of less than equal to <= object """
        if (not isinstance(other, Square)):
            return NotImplemented
        return (self.size <= other.size)

    def __eq__(self, other):
        """ rep. of equal to == object """
        if (not isinstance(other, Square)):
            return NotImplemented
        return (self.size == other.size)

    def __ne__(self, other):
        """ rep. of not equal to != object """
        if (not isinstance(other, Square)):
            return NotImplemented
        return (self.size != other.size)

    def __gt__(self, other):
        """ rep. of greater than > object """
        if (not isinstance(other, Square)):
            return NotImplemented
        return (self.size > other.size)

    def __ge__(self, other):
        """ rep. of greater than eequal to >= object """
        if (not isinstance(other, Square)):
            return NotImplemented
        return (self.size >= other.size)
