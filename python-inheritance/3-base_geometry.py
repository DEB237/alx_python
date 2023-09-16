"""
Module that defines the BaseGeometry class.
"""
class BaseGeometry:
    """
    An empty class representing the BaseGeometry.
    """
    def __dir__(self):
        # Get the list of attribute names from the class dictionary
        attrs = list(self.__class__.__dict__.keys())
        # Get the list of attribute names from the object dictionary
        attrs += list(self.__dict__.keys())
        # Remove duplicates and return sorted list
        return sorted(set(attrs))