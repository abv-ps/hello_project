"""
App configuration for the 'hello_app' Django application.

Defines the application name and default primary key field type
for models within this app.

Adheres to PEP8 style and includes type annotations where applicable.
"""

from django.apps import AppConfig


class HelloAppConfig(AppConfig):
    """Configuration class for the 'hello_app' application."""

    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'hello_app'
