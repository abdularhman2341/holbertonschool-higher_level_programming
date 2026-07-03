#!/usr/bin/python3
"""Module defining the Student class with serialization and deserialization."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if (isinstance(attrs, list) and
                all(isinstance(ele, str) for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): Dictionary where keys are attribute names and values
                         are the new values to set.
        """
        for key, value in json.items():
            setattr(self, key, value)
