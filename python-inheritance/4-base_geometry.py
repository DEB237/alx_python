"""
Module that defines a class
"""
class BaseGeometry:
    """
    This class represents the base geometry.
    """

    def __lt__(self, other):
        """
        Compares the geometry object with another object using the less-than operator.
        """
        pass

    def area(self):
        """
        Calculates the area of the geometry object.
        Raises:
            Exception: with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
