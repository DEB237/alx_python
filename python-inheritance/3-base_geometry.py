"""
Module that defines the BaseGeometry class.
"""
class BaseGeometry:
    def __init_subclass__(cls):
        """ Hide the init_subclass() method from the list of attributes
        and methods"""
        cls.__class__ = type(cls.__name__, (cls,), {})
