"""core/types/xbox_game_api.py
handle types for Xbox Game pass Data API
"""
# built-in
from typing_extensions import TypedDict


class Category(TypedDict):
    title: str
    description: str
    image_url: str
