from django.db import models


class Document(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    file = models.FileField(upload_to="documents/")

    version = models.IntegerField(default=1)

    project = models.ForeignKey(
        "projects.Project", on_delete=models.CASCADE, related_name="documents"
    )

    def __str__(self):
        return self.name
