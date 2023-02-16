#!/usr/bin/python3
"""Square module.
This moadule is a class Square tha defines a square by a private instance attribute size and a publice instamce attribute area
"""


class Square():
    """defined square"""

    def __init__(self, size=0):
        """Sets the required attributes for the square
        Args:
        size(int): the size of the square edge"""

        self.size = size

    @property
    def size(self):
        """get or set square size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be integer")

    def area(self):
        """retyurns thearea of the current square"""

        return self.__size ** 2
