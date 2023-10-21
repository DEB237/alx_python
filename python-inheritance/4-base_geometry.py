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
        def __dir__(cls) -> None:
        """
        control access to some inherited attributes
        """
        attributes = super().__dir__()
        n_attributes = []
        for attr in attributes:
            if attr != '__init_subclass__':
                n_attributes.append(attr)
        return n_attributes
    
    def area(self):
        """
        a method to raise an exception with a message
        """
        raise Exception("area() is not implemented")
