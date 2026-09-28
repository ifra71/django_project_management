from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Timeline
from .serializers import TimelineSerializer


class TimelineListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        timeline = Timeline.objects.all()

        serializer = TimelineSerializer(timeline, many=True)

        return Response(serializer.data)
