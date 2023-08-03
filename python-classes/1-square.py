""" 
This module defines the Square class.
"""
class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a square object with an optional size.
        Args:
            size (int, optional): The size of the square (default is 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
