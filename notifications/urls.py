from django.urls import path

from .views import MarkNotificationReadView, NotificationListView

urlpatterns = [
    path(
        "notifications/",
        NotificationListView.as_view(),
        name="notification-list",
    ),
    path(
        "notifications/<int:notification_id>/mark_read/",
        MarkNotificationReadView.as_view(),
        name="notification-mark-read",
    ),
]
