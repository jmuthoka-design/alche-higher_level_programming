#!/usr/bin/python3
"""Defines a custom list class."""


class MyList(list):
    """Represents a list with a method for displaying sorted values."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying it."""
        sorted_list = sorted(self)
        print(sorted_list)
        
