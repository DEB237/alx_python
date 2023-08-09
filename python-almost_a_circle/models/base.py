''' 
This module contains a class
'''


class Base:
    """
    Base class serves as the foundation for all other classes in the project.
    It manages the 'id' attribute and provides common functionality.

    Attributes:
        __nb_objects (int): Private class attribute to keep track of the number of instances.
        id (int): Public instance attribute representing the object's ID.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int, optional): The desired ID for the instance. Defaults to None.

        Notes:
            If 'id' is provided, sets 'id' as the instance's ID.
            If 'id' is not provided, increments '__nb_objects' and assigns the new value to 'id'.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
