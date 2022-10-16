"""user/apps.py
store metadata for the application configuration
"""
# third party
from django.apps import AppConfig


class YoutubeConfig(AppConfig):
    """
    youtube app metadata
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "youtube"
