"""youtube/admin.py
manage administration panel for youtube app
"""
# third party
from django.contrib import admin

# project modules
from youtube.models import Title, Tag, DebriefActu


admin.site.register(Title)
admin.site.register(Tag)
admin.site.register(DebriefActu)
