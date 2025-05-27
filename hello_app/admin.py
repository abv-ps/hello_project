"""
Admin configuration for the User model.

This module registers the User model with the Django admin interface,
enabling display and management of user instances via the admin panel.

It customizes the admin list view to show the 'name' field for each user.

Following PEP8 style and using type annotations for clarity.
"""

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    """Admin interface for the User model.

    Displays the 'name' field in the list view.
    """

    list_display: tuple[str, ...] = ('name',)
