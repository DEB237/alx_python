"""A function to check whether an instance inherits from a class"""

def inherits_from(obj, a_class):
    """
    My function
    Argument:
        obj
        a_class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
