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
        self.size = size

    @property
    def size(self):
        """
        Retrieve the current size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the current square's area.
        Returns:
            int: The area of the square (size^2).
        """
        return self.__size ** 2
    