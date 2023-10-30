#!/usr/bin/python3
"""
A module that contains the class Rectangle which inherits from BaseGeometry
"""


BaseGeometry = __import__("5-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that defines a Recatngle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Instantiation method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
