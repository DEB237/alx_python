"""
Module that defines a class
"""
class BaseGeometry:
    """
    This class represents the base geometry.
    """

    def area(self):
        """
        Calculates the area of the geometry object.
        Raises:
            Exception: with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
