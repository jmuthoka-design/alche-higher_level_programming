#!/usr/bin/python3
"""Define a Student class with a filtered JSON representation."""


class Student:
    """Represent a student with a first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with a first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the student's dictionary, optionally filtered by attrs."""
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {
                key: self.__dict__[key]
                for key in attrs
                if key in self.__dict__
            }
        return self.__dict__
