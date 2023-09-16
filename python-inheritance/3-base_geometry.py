"""
Module that defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    An empty class representing the BaseGeometry.
    """

    pass

    @classmethod
    def __dir__(cls):
        """
        Returns a list of attributes for the class, excluding init_subclass.
        """
        attributes = super().__dir__(cls)
        return [attr for attr in attributes if attr != 'init_subclass' and 'reduce']
      