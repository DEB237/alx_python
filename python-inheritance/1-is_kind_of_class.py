"""
Module that defines a function
"""
def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of or inherited from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of, or inherited from, the specified class,
              and False otherwise.
    """
    return isinstance(obj, a_class)
