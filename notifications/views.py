from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Notification
from .serializers import NotificationSerializer


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by(
            "-created_at"
        )


class MarkNotificationReadView(APIView):
    def put(self, request, notification_id):
        try:
            notification = Notification.objects.get(
                id=notification_id,
                user=request.user,
            )
        except Notification.DoesNotExist:
            return Response(
                {"message": "Notification not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        notification.mark_read = True
        notification.save(update_fields=["mark_read"])

        return Response(
            {
                "message": "Notification marked as read.",
                "notification": NotificationSerializer(notification).data,
            },
            status=status.HTTP_200_OK,
        )
