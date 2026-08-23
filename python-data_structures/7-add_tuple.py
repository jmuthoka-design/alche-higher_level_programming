#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add 2 tuples of integers, element by element

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        A tuple of 2 integers: the sum of the first elements and
        the sum of the second elements. Missing elements count as 0.
    """
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a0 + b0, a1 + b1)
