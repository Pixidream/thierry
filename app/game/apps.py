"""user/apps.py
store metadata for the application configuration
"""
# third party
from django.apps import AppConfig


class GameConfig(AppConfig):
    """
    game app metadata
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "game"
