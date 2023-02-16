"""a class Square that defines a square by a private instance attributes size and position and also by public instance methods area and my_print"""

class Square():
    """defined square"""

    def __init__(self, size=0, position=(0, 0)):
        """sets the required attributes for the square
        Args:
            size(int): the size of the square edge
            position(tuple): the coordinates of the square"""

        self.size = size
        self.position = position

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
            raise TypeError("size must be integer")

        @property
        def position(self):
            """get or set the position of the square"""
            return self.__position

        @position.setter
        def position(self, value):
            if type(value) is tuple and len(value) is 2 and \
                type(value[0]) is int and type(value[1]) is int and \
                    value[0] >= 0 and value[1] >= 0:
                    self.__position = value
            else:
                raise TypeError("posiiton must be tuple of 2 positive integers")

        def area(self):
            """returns the current area square"""
            return self.__size ** 2

        def my_print(self):
            """prints the square with the # charatcer ti stdout"""
            if self.__size > 0:
                for y in range(self.__position[1]):
                    print()
                for x in range(self.__size):
                    print(' ' * self.__position[0], end='')
                    print('#' * self.__size)
            else:
                print()
