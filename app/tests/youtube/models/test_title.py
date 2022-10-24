"""test/youtube/models/test_title.py
verify that I can create a title objects
"""
# built in
from typing import Dict

# third party
from django.test import TestCase

# project modules
from youtube.models import DebriefActu, Title


class TestTitle(TestCase):
    """
    handle all tests run on Title model
    """

    def setUp(self) -> None:
        """
        prepare data for tests to run
        """
        self.debrief = DebriefActu.objects.create(
            vid="toto", title="toto", release_date="2022-12-12", thumbnail="https://google.com"
        )
        Title.objects.create(
            name="titletitle", start_at="00:00:00", end_at="00:10:00", video=self.debrief
        )

    def _assert_titles(self, title: Title, params: Dict[str, str]):
        """
        private method that check assertions on title fields
        """
        self.assertIsInstance(title, Title)
        self.assertEqual(params["name"], title.name)
        self.assertEqual(params["start_at"], title.start_at)
        self.assertEqual(params["end_at"], str(title.end_at))
        self.assertEqual(params["video"], title.video)

    def test_01_create_title(self):
        """
        test that Title objects can be created
        """
        title = Title.objects.create(
            name="created_title", start_at="00:00:00", end_at="00:10:00", video=self.debrief
        )

        self._assert_titles(
            title,
            dict(name="created_title", start_at="00:00:00", end_at="00:10:00", video=self.debrief),
        )

    def test_02_get_title(self):
        """
        check that we can get a Title objects from database
        """
        title = Title.objects.get(name="titletitle")

        self._assert_titles(
            title,
            dict(name="titletitle", start_at="00:00:00", end_at="00:10:00", video=self.debrief),
        )

    def test_03_update_title(self):
        """
        check that we can update title objects in database
        """
        updated = Title.objects.filter(name="titletitle").update(end_at="00:20:00")

        self.assertEqual(updated, 1)

        title = Title.objects.get(name="titletitle")

        self._assert_titles(
            title,
            dict(name="titletitle", start_at="00:00:00", end_at="00:20:00", video=self.debrief),
        )

    def test_04_delete_title(self):
        """
        check that Title objects is properly deleted from database
        """
        Title.objects.get(name="titletitle").delete()

        self.assertRaises(Title.DoesNotExist, lambda: Title.objects.get(name="titletitle"))
