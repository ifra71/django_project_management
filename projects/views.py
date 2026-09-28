import logging

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from timeline.models import Timeline

from .models import Project
from .serializers import ProjectSerializer

logger = logging.getLogger(__name__)


class ProjectListCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.all()

        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            project = serializer.save()

            logger.info("Project created: %s", project.title)

            Timeline.objects.create(event_type="created", project=project)

            return Response(
                ProjectSerializer(project).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)

        serializer = ProjectSerializer(project)

        return Response(serializer.data)

    def put(self, request, project_id):
        project = Project.objects.get(id=project_id)

        serializer = ProjectSerializer(project, data=request.data)

        if serializer.is_valid():
            serializer.save()

            logger.info("Project updated: %s", project.title)

            Timeline.objects.create(event_type="updated", project=project)

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_id):
        project = Project.objects.get(id=project_id)

        Timeline.objects.create(event_type="deleted", project=project)

        project.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
