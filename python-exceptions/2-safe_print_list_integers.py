#!/usr/bin/python3
"""Module that prints integers from a list, skipping non-integers."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers found in my_list.

    Args:
        my_list (list): list containing elements of any type.
        x (int): number of elements to access in my_list.

    Returns:
        int: the real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count
