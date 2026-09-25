from django.db import models


class Timeline(models.Model):

    EVENT_TYPES = [
        ("created", "Created"),
        ("updated", "Updated"),
        ("deleted", "Deleted"),
    ]

    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)

    time = models.DateTimeField(auto_now_add=True)

    project = models.ForeignKey(
        "projects.Project", on_delete=models.CASCADE, related_name="timeline"
    )

    def __str__(self):
        return self.event_type
