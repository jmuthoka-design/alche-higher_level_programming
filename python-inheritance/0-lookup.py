#!/usr/bin/python3
"""Provides a function to list an object's attributes and methods."""


def lookup(obj):
    """Return a list of an object's attributes and methods."""
    return dir(obj)
