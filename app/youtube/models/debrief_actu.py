"""youtube/models/debrief_actu.py
DebriefActu model
"""
# third-party
from django.db.models import CharField, DateField, URLField, Model


class DebriefActu(Model):
    """
    data representation of DebriefActu
    """

    vid = CharField(max_length=256)
    title = CharField(max_length=256)
    release_date = DateField()
    thumbnail = URLField()

    def __str__(self) -> str:
        """
        return a representation of DebriefActu model
        """
        return f"{self.vid}-{self.title}"
