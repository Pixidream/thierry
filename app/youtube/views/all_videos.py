"""views/all_videos.py
return all videos stored in database (paginated)
"""
# third party
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_406_NOT_ACCEPTABLE

# project modules
from youtube.models import DebriefActu
from youtube.serializers import DebriefSerializer


@api_view()
def all_videos(request):
    """
    get debriefs from database and return them (paginated)
    """
    if request.version is None:
        return Response(
            {"error": "header 'Accept: application/json; version=1.0' required"},
            HTTP_406_NOT_ACCEPTABLE,
        )

    if request.version != "1.0":
        return Response(
            {"error": f"version {request.version} not supported"}, HTTP_406_NOT_ACCEPTABLE
        )

    paginator = PageNumberPagination()
    debriefs = DebriefActu.objects.all().order_by("-release_date")
    paginated_debriefs = paginator.paginate_queryset(debriefs, request)
    serializer = DebriefSerializer(paginated_debriefs, many=True)

    return paginator.get_paginated_response(serializer.data)
