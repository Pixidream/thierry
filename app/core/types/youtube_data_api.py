"""core/types/youtube_data_api.py
handle types for YouTube Data API
"""
# built-in
from typing import TypedDict, List, Dict


class PlaylistContentDetails(TypedDict):
    """
    represent contentDetails part of playlist list
    """

    videoId: str
    startAt: str
    endAt: str
    note: str
    videoPublishedAt: str


class PlaylistItem(TypedDict):
    """
    represent playlist item returned by YouTube Data API
    """

    contentDetails: PlaylistContentDetails
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
    thumbnails: Dict[str, Dict[str, str]]
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


class Tag(TypedDict):
    """
    tag dict created while parsing videos
    """

    name: str
    start_at: str
    end_at: str


class Title(TypedDict):
    """
    title dict created while parsing videos
    """

    name: str
    start_at: str
    end_at: str


class DebriefActus(TypedDict):
    """
    DebriefActu dict created while parsing videos
    """

    release_date: str
    tags: List[Tag]
    thumbnail: str
    title: str
    titles: List[Title]
    vid: str
