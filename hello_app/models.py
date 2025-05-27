"""
Defines the User model for storing simple user information.

This model contains a single field 'name' to hold the user's name.
It provides a string representation method to return the user's name.

The code follows PEP8 style guidelines with type annotations.
"""

from django.db import models


class User(models.Model):
    """A simple user model with a name field."""

    name: models.CharField = models.CharField(max_length=100)

    def __str__(self) -> str:
        """Return the string representation of the user.

        Returns:
            str: The name of the user.
        """
        return self.name
