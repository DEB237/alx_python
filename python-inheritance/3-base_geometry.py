"""
Module that defines the BaseGeometry class.
"""
class BaseGeometry:
    """
    An empty class representing the BaseGeometry.
    """
    def __init_subclass__(cls):
        pass  # Empty implementation to hide the __init_subclass__ method

    def __dir__(self):
        # Exclude the __init_subclass__ method from the list of attributes and methods
        return [attr for attr in self.__dict__.keys() if attr != '__init_subclass__']