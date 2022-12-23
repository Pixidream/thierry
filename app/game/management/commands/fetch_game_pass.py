"""game/management/commands/fetch_game_pass.py
management command to update game pass in db
"""
# built in
from typing import Any, Optional

# third party
from django.core.management.base import BaseCommand

# project modules
from core.utils import GamePassApi
from core.types import Category as CategoryI

from game.models import Category as CategoryModel


class Command(BaseCommand):
    """
    django management command
    """

    help = "fetch games from game pass and add them to database"

    def create_category(self, data: CategoryI) -> Optional[CategoryModel]:
        try:
            if CategoryModel.objects.filter(title=data["title"]).exists():
                self.stdout.write(
                    self.style.WARNING(f"category {data['title']!r} already exists !")
                )
                return None

            category = CategoryModel.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f"category {category.title!r} created"))

            return category

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"category failed to be created, reason: {e}"))

            return None

    def handle(self, *args: Any, **options: Any) -> None:
        all_category = GamePassApi.get_all_games()

        category = self.create_category(all_category)
