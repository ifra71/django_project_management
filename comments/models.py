# Create your models here.
from django.conf import settings
from django.db import models

from projects.models import Project
from tasks.models import Task


class Comment(models.Model):
    text = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="comments",
        null=True,
        blank=True,
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="comments",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Comment by {self.author.email}"
