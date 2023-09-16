"""
Module that defines the Square class.
"""


Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initializes a square object with the given size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
