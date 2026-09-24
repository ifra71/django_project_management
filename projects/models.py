from django.conf import settings
from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    start_date = models.DateField()

    end_date = models.DateField()

    team_members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="projects"
    )

    def __str__(self):
        return self.title