#!/usr/bin/python3
"""Convert a Python object into a JSON-formatted string."""

import json


def to_json_string(my_obj):
    """Return the JSON representation of a Python object."""
    return json.dumps(my_obj)
