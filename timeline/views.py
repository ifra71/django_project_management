from rest_framework import generics

from .models import Timeline
from .serializers import TimelineSerializer


class TimelineListView(generics.ListAPIView):
    serializer_class = TimelineSerializer

    def get_queryset(self):
        return Timeline.objects.filter(
            project__team_members=self.request.user
        ).order_by("-time")
