"""
Module that defines the Rectangle class.
"""

from 5-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    Represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle object with the given width and height.
        """
        self.width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.width, self.__height)

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.__height

    def __repr__(self):
        """
        Returns a string representation of the object.
        """
        return "Rectangle({}, {})".format(self.width, self.__height)
    