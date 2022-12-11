"""core/utils/pagination.py
custom PageNumberPagination
"""
# built in
from typing import Any

# third party
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Pagination(PageNumberPagination):
    """
    simple pagination that use only the number as "next" value
    and not the whole URL.
    """

    def get_paginated_response(self, data: Any) -> Response:
        return Response(
            {
                "next": self.page.next_page_number() if self.page.has_next() else None,
                "prev": self.page.previous_page_number() if self.page.has_previous() else None,
                "count": self.page.paginator.count,
                "results": data,
            }
        )
