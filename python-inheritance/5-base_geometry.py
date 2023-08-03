"""
Module that defines a class
"""


class BaseGeometry:
    """
    Base class for geometry shapes.
    """
    def area(self):
        """
        Placeholder method for calculating the area of a shape.
        This method should be implemented by subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that the given value is an integer greater than 0.
        
        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.
        
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle shape class.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle object with the given width and height.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
