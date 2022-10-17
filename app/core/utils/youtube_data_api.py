"""core/utils/youtube_data_api.py
map the youtube data api V3 to utils function
to consume in django app
"""
# built-in
# import os
# import re

# third party
# import googleapiclient.discovery
# import google.api_
# import isodate
#

# class YoutubeDataApi:
#     def __init__(self) -> None:
#         """
#         create google api client for youtube data api
#         """
#         self.api_service_name = "youtube"
#         self.api_version = "v3"
#         self.developer_key = os.getenv("YOUTUBE_API_KEY", "")
#         self.client = googleapiclient.discovery.build(
#             self.api_service_name, self.api_version, developerKey=self.developer_key
#         )
#
#     def get_infos(self, playlist_id: str, token: str = None) -> dict:
#         """
#         get playlist infos from youtube api
#         """
#         args = dict(
#             part="contentDetails",
#             playlistId=playlist_id,
#             maxResults=50,
#         )
#
#         if token:
#             args["pageToken"] = token
#
#         request = self.client.playlistItems().list(**args)
#
#         return request.execute()
#
#
# if __name__ == "__main__":
#     YoutubeDataApi().get_infos("PLshTqKdGwawUon5GsWo-Y4HsLgVCDnm3K", "token")
