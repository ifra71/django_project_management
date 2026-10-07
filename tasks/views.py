import logging

from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from common.permissions import IsProjectMemberOrReadOnly

from .models import Task
from .serializers import TaskSerializer

User = get_user_model()

logger = logging.getLogger(__name__)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsProjectMemberOrReadOnly]

    def get_queryset(self):
        return Task.objects.filter(project__team_members=self.request.user).distinct()

    @action(detail=True, methods=["post"])
    def assign(self, request, pk=None):
        task = self.get_object()

        user_id = request.data.get("user_id")

        if not user_id:
            return Response(
                {"message": "user_id is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"message": "User not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        if not task.project.team_members.filter(id=user.id).exists():
            return Response(
                {"message": "User is not a member of this project."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        task.assignee = user
        task.save()

        logger.info(
            "Task %s assigned to user %s by user %s",
            task.id,
            user.id,
            request.user.id,
        )

        serializer = self.get_serializer(task)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
