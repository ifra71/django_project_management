from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from projects.models import Project

from .models import Timeline


@receiver(post_save, sender=Project)
def create_project_timeline(sender, instance, created, **kwargs):
    if created:
        event_type = "created"
    else:
        event_type = "updated"

    Timeline.objects.create(
        project=instance,
        event_type=event_type,
    )


@receiver(post_delete, sender=Project)
def create_project_deleted_timeline(sender, instance, **kwargs):
    Timeline.objects.create(
        project=None,
        event_type="deleted",
    )
