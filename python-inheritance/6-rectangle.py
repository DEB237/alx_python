"""
Module that defines the Rectangle class.
"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle object with the given width and height.
        """

        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.__height = height