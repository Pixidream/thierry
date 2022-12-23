"""game/models/category.py
represent a game category
"""
# third-party
from django.db.models import Model, CharField


class Category(Model):
    """
    category model link to game
    """

    title = CharField(max_length=255)
    description = CharField(max_length=255)
    image_url = CharField(max_length=255)
