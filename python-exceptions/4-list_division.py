#!/usr/bin/python3
"""Module that divides two lists element by element."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide two lists element by element.

    Args:
        my_list_1 (list): the list of numerators.
        my_list_2 (list): the list of denominators.
        list_length (int): the length of the list to build.

    Returns:
        list: a new list with the results of each division.
    """
    new_list = []
    for i in range(list_length):
        divide = 0
        try:
            divide = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(divide)
    return new_list
