"""
Module that defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    An empty class representing the BaseGeometry.
    """

    def area(self):
        """
        Calculates the area of the geometry object.
        Raises:
            Exception: Always raised with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def __str__(self):
        """
        Returns a string representation of the geometry object.
        """
        return "[BaseGeometry]"

    def __repr__(self):
        """
        Returns a string representation of the object.
        """
        return "BaseGeometry()"

    @classmethod
    def __dir__(cls):
        """
        Returns a list of attributes for the class, excluding init_subclass.
        """
        attributes = super().__dir__()
        return [attr for attr in attributes if attr != 'init_subclass']

