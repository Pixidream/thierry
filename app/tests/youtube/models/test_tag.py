"""test/youtube/models/test_tag.py
verify that I can create a tag objects
"""
# built in
from typing import Dict

# third party
from django.test import TestCase

# project modules
from youtube.models import DebriefActu, Tag


class TestTag(TestCase):
    """
    handle all tests run on Tag model
    """

    def setUp(self) -> None:
        """
        prepare data for tests to run
        """
        self.debrief = DebriefActu.objects.create(
            vid="toto", title="toto", release_date="2022-12-12", thumbnail="https://google.com"
        )
        Tag.objects.create(
            name="tagtag", start_at="00:00:00", end_at="00:10:00", video=self.debrief
        )

    def _assert_tags(self, tag: Tag, params: Dict[str, str]):
        """
        private method that check assertions on tag fields
        """
        self.assertIsInstance(tag, Tag)
        self.assertEqual(params["name"], tag.name)
        self.assertEqual(params["start_at"], tag.start_at)
        self.assertEqual(params["end_at"], str(tag.end_at))
        self.assertEqual(params["video"], tag.video)

    def test_01_create_tag(self):
        """
        test that Tag objects can be created
        """
        tag = Tag.objects.create(
            name="created_tag", start_at="00:00:00", end_at="00:10:00", video=self.debrief
        )

        self._assert_tags(
            tag,
            dict(name="created_tag", start_at="00:00:00", end_at="00:10:00", video=self.debrief),
        )

    def test_02_get_tag(self):
        """
        check that we can get a Tag objects from database
        """
        tag = Tag.objects.get(name="tagtag")

        self._assert_tags(
            tag, dict(name="tagtag", start_at="00:00:00", end_at="00:10:00", video=self.debrief)
        )

    def test_03_update_tag(self):
        """
        check that we can update Tag objects in database
        """
        updated = Tag.objects.filter(name="tagtag").update(end_at="00:20:00")

        self.assertEqual(updated, 1)

        tag = Tag.objects.get(name="tagtag")

        self._assert_tags(
            tag, dict(name="tagtag", start_at="00:00:00", end_at="00:20:00", video=self.debrief)
        )

    def test_04_delete_tag(self):
        """
        check that Tag objects is properly deleted from database
        """
        Tag.objects.get(name="tagtag").delete()

        self.assertRaises(Tag.DoesNotExist, lambda: Tag.objects.get(name="tagtag"))
