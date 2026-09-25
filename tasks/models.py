from django.conf import settings
from django.db import models


class Task(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()
    STATUS_CHOICES = [
        ("open", "Open"),
        ("review", "Review"),
        ("working", "Working"),
        ("awaiting_release", "Awaiting Release"),
        ("waiting_qa", "Waiting QA"),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")

    project = models.ForeignKey(
        "projects.Project", on_delete=models.CASCADE, related_name="tasks"
    )

    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tasks",
    )

    def __str__(self):
        return self.title
