from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        if hasattr(obj, "author"):
            return obj.author == request.user

        if hasattr(obj, "user"):
            return obj.user == request.user

        return False


class IsProjectMemberOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        if hasattr(obj, "team_members"):
            return request.user in obj.team_members.all()

        if hasattr(obj, "project"):
            return request.user in obj.project.team_members.all()

        return False
