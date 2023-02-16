#!/usr/bin/python3
"""Square module.
This module is a class Square that defines a square by private instace attribute size with a given method.There is also a public instance method Area that returns the current square area
"""

class Square():
    """defined square"""

    def __init__(self, size=0):
        """sets the required attributes oif the square
        Args:
            size(int): size of square side
            area: current square area
        Raises:
            TypeError: if size is not integer
            ValueError: if size < 0"""

        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be integer")

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
