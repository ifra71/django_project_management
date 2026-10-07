from django.conf import settings
from django.db import models


class Notification(models.Model):
    text = models.TextField()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    mark_read = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"Notification for {self.user.email}"
