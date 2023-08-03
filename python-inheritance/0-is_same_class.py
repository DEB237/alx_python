"""
Module that defines a function
"""
def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.
    
    Args:
        obj: The object to check.
        a_class: The class to compare against.
        
    Returns:
        bool: True if the object is exactly an instance of the specified class,
              and False otherwise.
    """
    return type(obj) == a_class
