"""youtube/serializers/tag_serializer.py
handle Tag model serialization
"""
# third party
from rest_framework.serializers import ModelSerializer

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
        fields = "__all__"
        exclude = ["video"]
