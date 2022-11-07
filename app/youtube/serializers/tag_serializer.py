"""youtube/serializers/tag_serializer.py
handle Tag model serialization
"""
# third party
from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField

# project modules
from youtube.models import Tag


class TagSerializer(ModelSerializer):
    """
    create fields based on model
    """

    class Meta:
        """
        configure model serializer
        """

        model = Tag
        exclude = ["video"]


class TagDebriefSerializer(ModelSerializer):
    """
    create fields based on model
    with video hyperlink
    """

    video = HyperlinkedRelatedField(read_only=True, view_name="video")

    class Meta:
        """
        configure model serializer
        """

        model = Tag
        fields = "__all__"
