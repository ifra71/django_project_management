from django.urls import path

from .views import ProjectDetailView, ProjectListCreateView

urlpatterns = [
    path(
        "projects/",
        ProjectListCreateView.as_view(),
        name="projects",
    ),
    path(
        "projects/<int:project_id>/", ProjectDetailView.as_view(), name="project-detail"
    ),
]
