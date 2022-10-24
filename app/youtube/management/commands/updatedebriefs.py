"""youtube/managment/commands/updatedebriefs.py
managment command that update database with latest debriefs actu
"""
# build in
from typing import Any

# third party
from django.core.management.base import BaseCommand

# project package
# from core.utils import YoutubeDataApi


class Command(BaseCommand):
    """
    run with manage.py updatedebriefs
    """

    help = "parse videos from Debrief Actu playlist and add them to database"

    def handle(self, *args: Any, **options: Any) -> None:
        """
        load the youtube data api and fetch videos id from Debrief actu playlist
        """
        # yt_api = YoutubeDataApi()
        return
