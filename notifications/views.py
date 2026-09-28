import logging

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Notification
from .serializers import NotificationSerializer

logger = logging.getLogger(__name__)


class NotificationListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.all()

        serializer = NotificationSerializer(notifications, many=True)

        return Response(serializer.data)


class MarkNotificationReadView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, notification_id):
        notification = Notification.objects.get(id=notification_id)

        notification.mark_read = True
        notification.save()

        logger.info("Notification marked as read: %s", notification.id)

        serializer = NotificationSerializer(notification)

        return Response(serializer.data)
