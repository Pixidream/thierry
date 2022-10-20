"""tests/core/test_youtube_data_api.py
unittest methods from app/core/utils/youtube_data_api.py
"""
# built in
from unittest import TestCase
from os import getenv

# project modules
from core.utils import YoutubeDataApi


class YoutubeDataApiTest(TestCase):
    """
    class that handle all tests
    """

    def setUp(self) -> None:
        """
        Method called to prepare the test fixture
        """
        self.yt_api = YoutubeDataApi()

    def test_get_infos(self):
        """
        run the get_infos method and check that kind is valid
        and then that there is a least on item returned
        """
        infos = self.yt_api.get_infos(getenv("DEBRIEF_ACTU_PLAYLIST_ID"))
        self.assertEqual(infos["kind"], "youtube#playlistItemListResponse")
        self.assertTrue(len(infos["items"]) > 0)
