"""
thierry URL Configuration
"""
# third party
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/youtube/", include(("youtube.urls", "youtube"), namespace="youtube")),
]
