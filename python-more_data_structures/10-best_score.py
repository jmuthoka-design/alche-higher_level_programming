#!/usr/bin/python3
def best_score(a_dictionary):
    """Return the key with the biggest integer value in a dictionary

    Args:
        a_dictionary: dictionary with integer values

    Returns:
        The key associated with the highest value, or None if
        a_dictionary is None or empty
    """
    if not a_dictionary:
        return None
    best_key = None
    best_value = None
    for key in a_dictionary:
        if best_value is None or a_dictionary[key] > best_value:
            best_value = a_dictionary[key]
            best_key = key
    return best_key
