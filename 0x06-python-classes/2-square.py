#!/usr/bin/python3
""" A class Square that defines a square by
- Private atttribute: size
- Instantion with optional size: def __init__(self, size=0)
  size must be an integer, otherwise raise TypeError exception
  with message "size must be an integer"
  if size is less than 0, raise a ValueError exception message
  "size must be >= 0"
"""


class Square:
    """ clas square """
    def __init__(self, size=0):
        """ initialize private attribute size """
        if type(size) != type(1):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
