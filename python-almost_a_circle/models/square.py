#!/usr/bin/python3
"""
A module that contains the Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation method"""
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    def __str__(self):
        """
        Defines the value that will be returned when print() and str() are used
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """Public getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Public setter method for size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
