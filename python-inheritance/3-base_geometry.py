"""
Module that defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    An empty class representing the BaseGeometry.
    """

    def __init_subclass__(cls):
        pass

    def area(self):
        pass

    @classmethod
    def __dir__(cls):
        """
        Returns a list of attributes for the class, excluding init_subclass.
        """
        attributes = super().__dir__()
        return [attr for attr in attributes if attr != 'init_subclass']