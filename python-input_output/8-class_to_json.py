#!/usr/bin/python3
"""Return the dictionary representation of an object for JSON serialization."""


def class_to_json(obj):
    """Return a dictionary containing an object's serializable attributes."""
    return obj.__dict__

