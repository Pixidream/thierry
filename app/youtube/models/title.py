"""youtube/models/title.py
represent titles of DebriefActu
"""
# third-party
from django.db.models import Model, CharField, ForeignKey, CASCADE

# project modules
from .debrief_actu import DebriefActu


class Title(Model):
    """
    Title representation
    """

    name = CharField(max_length=256)
    start_at = CharField(max_length=12)
    end_at = CharField(max_length=12)
    video = ForeignKey(DebriefActu, related_name="titles", on_delete=CASCADE)

    def __str__(self) -> str:
        """
        string repr of title
        """
        return self.name
