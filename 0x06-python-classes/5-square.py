#!/usr/bin/python3
"""Square Module.
This module is a class Square that defines a square by a private instnacxe attribute size, a public instnace method area and a public instnace method my_print that prints in the stdout the square with character #
"""

class Square():
    """defined square"""

    def __init__(self, size=0):
        """sets the necessary attributes for the Square object
        Args:
            size(int): size of square edge"""

        self.size = size

    @property
    def size(self):
        """get or set the square size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must ne integer")

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints the square with character # to stdout"""
        if self.__size > 0:
            for x in range(self.__size):
                print('#' * self.__size)
        else:
            print()
