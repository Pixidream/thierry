"""youtube/serializers/debrief_serializer.py
handler Debrief model serialization
"""
# third party
from rest_framework.serializers import ModelSerializer

# project modules
from youtube.models.debrief_actu import DebriefActu


class DebriefSerializer(ModelSerializer):
    """
    map model fields to Serializer fields
    """

    class Meta:
        """
        configure serializer
        """

        model = DebriefActu
        fields = "__all__"
