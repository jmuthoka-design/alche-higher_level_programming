#!/usr/bin/python3
"""Defines a custom list class."""


class MyList(list):
    """A custom list class."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
        
