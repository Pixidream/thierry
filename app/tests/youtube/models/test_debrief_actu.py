"""test/youtube/models/test_debrief_actu.py
verify that i can create a debrief actu objects
"""
# built-in
from datetime import date
from typing import Dict

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
        DebriefActu.objects.create(
            vid="toto", title="toto", release_date="12-12-2022", thumbnail="https://google.com"
        )

    def _assert_debrief(self, debrief: DebriefActu, params: Dict[str, str]):
        self.assertIsInstance(debrief, DebriefActu)
        self.assertEqual(params["vid"], debrief.vid)
        self.assertEqual(params["title"], debrief.title)
        self.assertEqual(params["release_date"], debrief.release_date)
        self.assertEqual(params["thumbnail"], debrief.thumbnail)

    def test_01_create_debrief(self):
        """
        check that DebriefActu can be registered to database
        """
        debrief = DebriefActu.objects.create(**self.dummy)
        self._assert_debrief(debrief, self.dummy)

    def test_02_get_debrief(self):
        """
        check that we can get a debrief from database
        """
        debrief = DebriefActu.objects.get(vid="toto")
        self._assert_debrief(
            debrief,
            dict(
                vid="toto", title="toto", release_date="12-12-2022", thumbnail="https://google.com"
            ),
        )
