#!/usr/bin/python3
"""Create a Python object from a JSON-formatted file."""

import json


def load_from_json_file(filename):
    """Return the Python object represented by a JSON file."""
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
