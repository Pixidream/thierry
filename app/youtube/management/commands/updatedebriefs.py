"""youtube/managment/commands/updatedebriefs.py
managment command that update database with latest debriefs actu
"""
# build in
from typing import Any

# third party
from django.core.management.base import BaseCommand

# project package
from core.utils import YoutubeDataApi

from youtube.models import Tag as TagModel, DebriefActu as DebriefActuModel, Title as TitleModel


class Command(BaseCommand):
    """
    run with manage.py updatedebriefs
    """

    help = "parse videos from Debrief Actu playlist and add them to database"

    def handle(self, *args: Any, **options: Any) -> None:
        """
        load the youtube data api and fetch videos id from Debrief actu playlist
        """
        yt_api = YoutubeDataApi()

        debriefs = yt_api.serialize_debriefs_from_api()
        counter = dict(debrief=0, tag=0, title=0, error=0)

        for debrief in debriefs:
            tags = debrief["tags"]
            titles = debrief["titles"]

            debrief.pop("tags")
            debrief.pop("titles")

            try:
                debrief["release_date"] = str(debrief["release_date"]).split("T", maxsplit=1)[0]
                created_debrief = DebriefActuModel.objects.create(**debrief)
                counter["debrief"] += 1

                for tag in tags:
                    TagModel.objects.create(**tag, video=created_debrief)
                    counter["tag"] += 1

                for title in titles:
                    TitleModel.objects.create(**title, video=created_debrief)
                    counter["title"] += 1

            except Exception as error:  # pylint: disable=broad-except
                self.stderr.write(self.style.ERROR(error))
                counter["error"] += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"{counter['debrief']} debriefs, {counter['title']} titles,"
                f"{counter['tag']} tags synced and {counter['error']} failed"
            )
        )
