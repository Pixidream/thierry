"""youtube/serializers/debrief_serializer.py
handler Debrief model serialization
"""
# third party
from rest_framework.serializers import ModelSerializer

# project modules
from youtube.models.debrief_actu import DebriefActu
from .tag_serializer import TagSerializer
from .title_serializer import TitleSerializer


class DebriefSerializer(ModelSerializer):
    """
    map model fields to Serializer fields
    """

    tags = TagSerializer(many=True, read_only=True)
    titles = TitleSerializer(many=True, read_only=True)

    class Meta:
        """
        configure serializer
        """

        model = DebriefActu
        fields = "__all__"
