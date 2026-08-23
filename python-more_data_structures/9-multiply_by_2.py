#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by 2

    Args:
        a_dictionary: dictionary with integer values

    Returns:
        A new dictionary with the same keys, each value doubled.
        The original dictionary is not modified.
    """
    new_dictionary = {}
    for key in a_dictionary:
        new_dictionary[key] = a_dictionary[key] * 2
    return new_dictionary
