#!/usr/bin/python3
"""Save a Python object to a file using JSON representation."""

import json


def save_to_json_file(my_obj, filename):
    """Write a Python object as JSON to a text file."""
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
