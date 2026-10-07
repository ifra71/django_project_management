from django.urls import path

from .views import TimelineListView

urlpatterns = [
    path(
        "timeline/",
        TimelineListView.as_view(),
        name="timeline-list",
    ),
]
