#!/usr/bin/python3
"""Square module.
This module is a class Square that defines a square by private instance attribute size with a given init method
"""


class Square():
    """defined square"""

    def __init__(self, size=0):
        """Sets the required attributes for the square object
        Args:
            size: the size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size < 0
        """

        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("Size must be >= 0")
        else:
            raise TypeError("size must be integer")
