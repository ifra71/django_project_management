from django.urls import path

from .views import AssignTaskView, TaskDetailView, TaskListCreateView

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="tasks"),
    path("tasks/<int:task_id>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:task_id>/assign/", AssignTaskView.as_view(), name="task-assign"),
]
