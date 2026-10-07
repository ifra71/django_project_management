from django.conf import settings
from django.db import models

from projects.models import Project


class Task(models.Model):
    STATUS_CHOICES = [
        ("open", "Open"),
        ("review", "Review"),
        ("working", "Working"),
        ("awaiting_release", "Awaiting Release"),
        ("waiting_qa", "Waiting QA"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="open",
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tasks",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
