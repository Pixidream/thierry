"""youtube/serializers/title_serializer.py
handler Title model serialization
"""
# third party
from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField

# project modules
from youtube.models.title import Title


class TitleSerializer(ModelSerializer):
    """
    map model fields to serializer fields
    """

    class Meta:
        """
        configure serializer
        """

        model = Title
        exclude = ["video"]


class TitleDebriefSerializer(ModelSerializer):
    """
    map model fields to serializer fields
    also hyperlink video field
    """

    video = HyperlinkedRelatedField(read_only=True, view_name="video")

    class Meta:
        """
        configure serializer
        """

        model = Title
        fields = "__all__"
