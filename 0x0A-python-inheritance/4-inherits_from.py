#!/usr/bin/python3
"is an instance of class or superclass"


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False."""

    if isinstance(obj, a_class):
        return True
    for base in obj.__class__.__bases__:
        if inherits_from(base, a_class):
            return True
    return False
