"""youtube/urls.py
handle urls of youtube application
"""
# third party
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import all_videos


urlpatterns = format_suffix_patterns([path("videos/", all_videos)])
