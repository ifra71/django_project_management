from rest_framework import generics

from common.permissions import IsProjectMemberOrReadOnly

from .models import Project
from .serializers import ProjectSerializer


class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(team_members=self.request.user).distinct()

    def perform_create(self, serializer):
        project = serializer.save()
        project.team_members.add(self.request.user)


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsProjectMemberOrReadOnly]
    lookup_url_kwarg = "project_id"
