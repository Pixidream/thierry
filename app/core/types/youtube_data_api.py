"""core/types/youtube_data_api.py
handle types for youtube data api
"""
# built-in
from typing import TypedDict, List, Dict


class PlaylistItem(TypedDict):
    """
    represent playlist item returned by youtube api
    """

    contentDetails: Dict[str, str]
    etag: str
    id: str
    kind: str


class PlaylistInfos(TypedDict):
    """
    represent playlist infos return by youtube
    """

    etag: str
    items: List[PlaylistItem]
    kind: str
    nextPageToken: str
    pageInfo: Dict[str, int]
