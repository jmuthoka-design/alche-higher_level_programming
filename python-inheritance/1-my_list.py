#!/usr/bin/python3
"""Defines the MyList class."""


class MyList(list):
    """A list subclass with a method to print a sorted copy."""

    def print_sorted(self):
        """Print the list in ascending order."""
        new_list = self.copy()
        new_list.sort()
        print(new_list)
        
