"""core/utils/game_pass_api.py
map the game pass APIs to utils function
to consume in django app
"""
# built in
import json
from typing import Any, Dict

# third party
import requests

# project modules
from core.types import Category


class GamePassApi:
    """
    util function to fetch games in game pass
    """

    @classmethod
    def get_all_games(cls) -> Category:
        res: requests.Response = requests.get(
            "https://catalog.gamepass.com/sigls/v2?id=29a81209-df6f-41fd-a528-2ae6b91f719c&language=en-us&market=US"
        )
        content: Any = json.loads(res.content.decode("utf-8"))
        category: Dict[str, str] = content.pop(0)
        game_ids: str = ",".join([game["id"] for game in content])

        game_category: Category = {
            "description": category["description"],
            "image_url": category["imageUrl"],
            "title": category["title"],
        }

        print(game_category)

        return game_category
