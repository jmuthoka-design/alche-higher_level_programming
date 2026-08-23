#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieve an element from a list like in C

    Args:
        my_list: the list to access
        idx: the index of the element to retrieve

    Returns:
        The element at idx, or None if idx is negative or out of range
    """
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
