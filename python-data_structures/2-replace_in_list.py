#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position

    Args:
        my_list: the list to modify
        idx: the index of the element to replace
        element: the new value to place at idx

    Returns:
        my_list, modified if idx is valid, unchanged otherwise
    """
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
