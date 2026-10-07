from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from notifications.models import Notification
from projects.models import Project


@shared_task
def send_project_deadline_reminders():
    today = timezone.now().date()
    tomorrow = today + timedelta(days=1)

    projects = Project.objects.filter(
        end_date__in=[today, tomorrow],
    )

    for project in projects:
        for user in project.team_members.all():
            notification_text = (
                f"Project deadline reminder: {project.title} "
                f"ends on {project.end_date}."
            )

            Notification.objects.get_or_create(
                user=user,
                text=notification_text,
            )

    return "Project deadline reminders processed."
