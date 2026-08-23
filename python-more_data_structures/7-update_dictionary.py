#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replace or add a key/value in a dictionary

    Args:
        a_dictionary: the dictionary to update
        key: the key to set (always a string)
        value: the value to associate with key (any type)

    Returns:
        a_dictionary, updated in place
    """
    a_dictionary[key] = value
    return a_dictionary
