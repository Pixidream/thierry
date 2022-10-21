"""core/utils/youtube_data_api.py
map the youtube data api V3 to utils function
to consume in django app
"""
# built-in
import os
from typing import List, Optional

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

    def get_infos(self, playlist_id: str, token: Optional[str] = None) -> PlaylistInfos:
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
            self.client.videos()  # pylint: disable=E1101
            .list(part="contentDetails,snippet,status", id=ids)
            .execute()
        )

    def _get_all_vids(
        self, token: Optional[str] = None, ids: Optional[List[List[str]]] = None
    ) -> List[str]:
        """
        recursive function that fetch all ids in all pages of
        playlist infos
        """
        vids: List[List[str]] = ids or []
        infos = self.get_infos(os.getenv("DEBRIEF_ACTU_PLAYLIST_ID", ""), token=token)

        vids.append([])
        vids[-1].extend(item["contentDetails"]["videoId"] for item in infos["items"])

        if "nextPageToken" in infos:
            self._get_all_vids(infos.get("nextPageToken"), vids)

        return [",".join(id_list) for id_list in vids]

    def serialize_debriefs_from_api(self):
        """
        fetch all videos from the YouTube Data API
        create dict that represent Debrief Model,
        parse the description to get title and tags
        """
        actus = []
        tag_regex = r"^-(?P<tag>[\w\s]+)-?$\n(?P<time_code>[\d{2}:]{4,8})"
        title_regex = r"^(?P<time_code>[\d{2}:]{4,8})\s(?P<title>.*)$"

        vids = self._get_all_vids()
        videos = [self.get_videos(vid) for vid in vids]

        print(videos, actus, tag_regex, title_regex)
