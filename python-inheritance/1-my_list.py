#!/usr/bin/python3
"""Defines a custom list class that can print a sorted copy."""


class MyList(list):
    """Represents a list with an additional sorting display method."""

    def print_sorted(self):
        """Prints the list in ascending order without changing the original."""
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
        
