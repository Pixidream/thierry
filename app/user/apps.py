"""user/apps.py
store metadata for the application configuration
"""
# third party
from django.apps import AppConfig


class UserConfig(AppConfig):
    """
    user app metadata
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "user"
    label = "user"
    verbose_name = "User"
