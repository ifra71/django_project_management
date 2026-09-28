import logging

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer

logger = logging.getLogger(__name__)


class TaskListCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.all()

        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            task = serializer.save()

            logger.info("Task created: %s", task.title)

            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)

        serializer = TaskSerializer(task)

        return Response(serializer.data)

    def put(self, request, task_id):
        task = Task.objects.get(id=task_id)

        serializer = TaskSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id):
        task = Task.objects.get(id=task_id)

        task.delete()

        return Response(
            {"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class AssignTaskView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)

        assignee_id = request.data.get("assignee")

        task.assignee_id = assignee_id
        task.save()

        logger.info("Task assigned: %s", task.title)

        return Response(TaskSerializer(task).data)
