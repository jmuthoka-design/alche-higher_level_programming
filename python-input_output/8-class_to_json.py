#!/usr/bin/python3
"""Return an object's dictionary representation for JSON serialization."""


def class_to_json(obj):
    """Return a dictionary containing the object's serializable attributes."""
    return obj.__dict__
