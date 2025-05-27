"""
URL configuration for the 'hello_app' Django application.

Maps the root URL to the home view.

Follows PEP8 conventions and includes type annotations where applicable.
"""

from django.urls import path
from .views import home

urlpatterns: list = [
    path('', home, name='home'),
]
