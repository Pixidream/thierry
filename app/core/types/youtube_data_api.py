"""core/types/youtube_data_api.py
handle types for YouTube Data API
"""
# built-in
from typing import TypedDict, List, Dict


class PlaylistItem(TypedDict):
    """
    represent playlist item returned by YouTube Data API
    """

    contentDetails: Dict[str, str]
    etag: str
    id: str
    kind: str


class PlaylistInfos(TypedDict):
    """
    represent playlist infos return by YouTube Data API
    """

    etag: str
    items: List[PlaylistItem]
    kind: str
    nextPageToken: str
    pageInfo: Dict[str, int]


class VideoSnippet(TypedDict):
    """
    represent snippet part of VideoItem
    """

    publishedAt: str
    channelId: str
    title: str
    description: str
    thumbnails: Dict[str, str]
    channelTitle: str
    tags: List[str]
    categoryId: str
    liveBroadcastContent: str
    defaultLanguage: str
    localized: Dict[str, str]
    defaultAudioLanguage: str


class VideoContentDetails(TypedDict):
    """
    contentDetails part of VideoItem
    """

    duration: str
    dimension: str
    definition: str
    caption: str
    licensedContent: bool
    regionRestriction: Dict[str, List[str]]


class VideoStatus(TypedDict):
    """
    Status part of VideoItem
    """

    uploadStatus: str
    failureReason: str
    rejectionReason: str
    privacyStatus: str
    publishAt: str
    license: str
    embeddable: bool
    publicStatsViewable: bool
    madeForKids: bool
    selfDeclaredMadeForKids: bool


class VideoStatistics(TypedDict):
    """
    stat part of VideoItem
    """

    viewCount: str
    likeCount: str
    dislikeCount: str
    favoriteCount: str
    commentCount: str


class VideoItem(TypedDict):
    """
    represent video item return by YouTube Data API
    """

    kind: str
    etag: str
    id: str
    snippet: VideoSnippet
    contentDetails: VideoContentDetails
    status: VideoStatus
    statistics: VideoStatistics


class VideoResponse(TypedDict):
    """
    represent the response from YouTube Data Api when listing videos
    """

    kind: str
    etag: str
    nextPageToken: str
    prevPageToken: str
    pageInfo: Dict[str, int]
    items: List[VideoItem]
