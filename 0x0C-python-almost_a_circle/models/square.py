#!/usr/bin/python3
"""Module that created a Class Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """instations Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Function that return a str to print"""
        return ("[Square] ({}) {}/{} - \
{}".format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Function property of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Fucntion setter that size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Function that update the attributes that args"""
        for position, arg in enumerate(args):
            if position == 0:
                self.id = arg
            elif position == 1:
                self.width = arg
            elif position == 2:
                self.x = arg
            else:
                self.y = arg
        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'size':
                self.width = value
            elif key == 'x':
                self.x = value
            elif key == 'y':
                self.y = value

    def to_dictionary(self):
        """Function that return a dictionary with the attributtes"""
        dictionary = {'id': self.id, 'size': self.width, '\
x': self.x, 'y': self.y}
        return dictionary
