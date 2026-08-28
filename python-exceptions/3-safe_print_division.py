#!/usr/bin/python3
"""Module that divides two integers safely."""


def safe_print_division(a, b):
    """Divide a by b and print the result.

    Args:
        a (int): the dividend.
        b (int): the divisor.

    Returns:
        float: the result of the division, or None if it failed.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error")
    finally:
        print("Inside result: {}".format(result))
    return result
