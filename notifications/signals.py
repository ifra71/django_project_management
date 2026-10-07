from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from notifications.models import Notification
from tasks.models import Task


@receiver(pre_save, sender=Task)
def remember_previous_assignee(sender, instance, **kwargs):
    if not instance.pk:
        instance._previous_assignee_id = None
        return

    try:
        old_task = Task.objects.get(pk=instance.pk)
        instance._previous_assignee_id = old_task.assignee_id
    except Task.DoesNotExist:
        instance._previous_assignee_id = None


@receiver(post_save, sender=Task)
def create_assignment_notification(sender, instance, created, **kwargs):
    previous_assignee_id = getattr(
        instance,
        "_previous_assignee_id",
        None,
    )

    current_assignee_id = instance.assignee_id

    assignee_changed = previous_assignee_id != current_assignee_id

    if current_assignee_id and (created or assignee_changed):
        Notification.objects.create(
            user=instance.assignee,
            text=f"You have been assigned the task: {instance.title}",
        )
