#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a copy of a list at a specific position

    Args:
        my_list: the original list (never modified)
        idx: the index of the element to replace in the copy
        element: the new value to place at idx

    Returns:
        A new list with the element replaced if idx is valid,
        otherwise a copy of the original list
    """
    new_list = my_list[:]
    if idx < 0:
        return new_list
    if idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
