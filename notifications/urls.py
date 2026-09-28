from django.urls import path

from .views import MarkNotificationReadView, NotificationListView

urlpatterns = [
    path("notifications/", NotificationListView.as_view(), name="notifications"),
    path(
        "notifications/<int:notification_id>/read/",
        MarkNotificationReadView.as_view(),
        name="notification-read",
    ),
]
