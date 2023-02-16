#!/usr/bin/python3
"""Square Module.
This module contains class Square that defines a square by a private instance attribute size.
"""

class Square():
    """defined square"""

    def __init__(self, size):
        """sets the required attributes for the square.
        Args:
            size (int): the size of the square.
        """
        self.__size = size
