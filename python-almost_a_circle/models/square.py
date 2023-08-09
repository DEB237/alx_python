'''
This module contains a class
'''

from models.rectangle import Rectangle
'''
Importing Base class from base
'''

class Square(Rectangle):
    """
    Square class inherits from Rectangle and represents a square shape.

    Attributes:
        id (int): The ID of the square.
        size (int): The length of the sides of the square.
        x (int): The x-coordinate position of the square.
        y (int): The y-coordinate position of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The length of the sides of the square.
            x (int, optional): The x-coordinate position of the square. Defaults to 0.
            y (int, optional): The y-coordinate position of the square. Defaults to 0.
            id (int, optional): The ID of the square. Defaults to None.

        Notes:
            Calls the super class with the necessary arguments to utilize the logic of the init in the Rectangle class.
            Assigns each argument (size, x, y) to the corresponding attribute.
        """
        super().__init__(size, size, x, y, id)  # Call super() with size as both width and height
        self.size = size

    def __str__(self):
        """
        Returns the string representation of the square.
        Returns:
            str: The string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
        Get the size (side length) of the square.
        Returns:
            int: The length of the sides of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size (side length) of the square.

        Args:
            value (int): The new length of the sides of the square.

        Raises:
            TypeError: If the value is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
           raise TypeError("Size must be a positive integer.")
        

        self.width = value
        self.height = value
