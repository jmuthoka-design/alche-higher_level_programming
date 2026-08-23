#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of a value in a copy of a list

    Args:
        my_list: the original list (never modified)
        search: the value to search for
        replace: the value to replace it with

    Returns:
        A new list with every occurrence of search replaced by replace
    """
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
