from django.conf import settings
from django.db import models


class Comment(models.Model):

    text = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    task = models.ForeignKey(
        "tasks.Task", on_delete=models.CASCADE, related_name="comments"
    )

    project = models.ForeignKey(
        "projects.Project", on_delete=models.CASCADE, related_name="comments"
    )

    def __str__(self):
        return self.text
