from rest_framework import serializers

from .models import Timeline


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = [
            "id",
            "event_type",
            "time",
            "project",
        ]
        read_only_fields = [
            "id",
            "event_type",
            "time",
            "project",
        ]
