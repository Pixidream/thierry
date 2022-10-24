"""test/youtube/models/test_debrief_actu.py
verify that i can create a debrief actu objects
"""
# built-in
from datetime import date

# third-party
from django.test import TestCase

# project modules
from youtube.models import DebriefActu


class TestDebriefActu(TestCase):
    """
    TestCase for Debrief Actu
    """

    def setUp(self) -> None:
        self.dummy = {
            "vid": "yol-kVahVWQ",
            "title": "Debrief d'actu : Les Sims 5 pourrait être multi, A plague Tale : Requiem...",
            "release_date": str(date.today()),
            "thumbnail": "https://i.ytimg.com/vi/yol-kVahVWQ/hqdefault.jpg",
        }

        self.debrief = None

    def test_01_create_debrief(self):
        """
        check that DebriefActu can be registered to database
        """
        debrief = DebriefActu(**self.dummy)
        debrief.save()

        self.assertIsInstance(debrief, DebriefActu)
        self.assertEqual(self.dummy["vid"], debrief.vid)
        self.assertEqual(self.dummy["title"], debrief.title)
        self.assertEqual(self.dummy["release_date"], debrief.release_date)
        self.assertEqual(self.dummy["thumbnail"], debrief.thumbnail)
