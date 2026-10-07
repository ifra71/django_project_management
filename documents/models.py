from django.db import models

from projects.models import Project


class Document(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    file = models.FileField(
        upload_to="documents/",
    )

    version = models.CharField(
        max_length=50,
        default="1.0",
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="documents",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
