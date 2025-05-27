"""
View definitions for the 'hello_app' Django application.

Contains the home view which fetches all User records and renders
them in the 'hello_app/home.html' template.

Adheres to PEP8 style guidelines and includes type annotations.
"""

from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import User


def home(request: HttpRequest) -> HttpResponse:
    """Render the home page displaying all users.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The HTTP response with the rendered template.
    """
    users = User.objects.all()
    context: dict[str, Any] = {'users': users}
    return render(request, 'hello_app/home.html', context)
