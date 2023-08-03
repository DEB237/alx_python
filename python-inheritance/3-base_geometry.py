"""
Module that defines a class
"""
class BaseGeometry:
    """
    An empty class representing the base geometry.
    """
    def __init_subclass__(cls):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __subclasshook__(self, subclass):
        pass
    