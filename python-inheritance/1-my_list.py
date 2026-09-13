#!/usr/bin/python3
"""Defines a custom list class."""


class MyList(list):
    """A list with a method to print its contents in sorted order."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
        
