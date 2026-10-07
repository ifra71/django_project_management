from django.db import models

from projects.models import Project


class Timeline(models.Model):
    EVENT_TYPE_CHOICES = [
        ("created", "Created"),
        ("updated", "Updated"),
        ("deleted", "Deleted"),
    ]

    event_type = models.CharField(
        max_length=20,
        choices=EVENT_TYPE_CHOICES,
    )

    time = models.DateTimeField(
        auto_now_add=True,
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="timeline_events",
    )

    def __str__(self):
        return f"{self.event_type} - {self.project}"
