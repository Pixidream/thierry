"""core/utils/youtube_data_api.py
map the youtube data api V3 to utils function
to consume in django app
"""
# built-in
import os

# third party
import googleapiclient.discovery

# project modules
from core.types import PlaylistInfos, VideoResponse


class YoutubeDataApi:
    """
    wrapper around the YouTube api
    """

    def __init__(self) -> None:
        """
        create google api client for youtube data api
        """
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.developer_key = os.getenv("YOUTUBE_API_KEY", "")
        self.client = googleapiclient.discovery.build(
            self.api_service_name, self.api_version, developerKey=self.developer_key
        )

    def get_infos(self, playlist_id: str, token: str = None) -> PlaylistInfos:
        """
        get playlist infos from YouTube api
        """
        return (
            self.client.playlistItems()  # pylint: disable=E1101
            .list(part="contentDetails", playlistId=playlist_id, maxResults=50, pageToken=token)
            .execute()
        )

    def get_videos(self, ids: str) -> VideoResponse:
        """
        retrieve infos for each video of the playlist (by group of 50 max)

        Parameters:
        ----------
        ids: list of comma separated video ids
        """
        return (
            self.client.videos().list(part="contentDetails,snippet,status", id=ids).execute()  # pylint: disable=E1101
        )
