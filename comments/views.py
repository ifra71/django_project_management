from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.helpers import get_object_or_none
from common.permissions import IsOwnerOrReadOnly

from .models import Comment
from .serializers import CommentSerializer


class CommentListCreateView(APIView):
    def get(self, request):
        comments = Comment.objects.filter(author=request.user).order_by("-created_at")

        serializer = CommentSerializer(
            comments,
            many=True,
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            task = serializer.validated_data.get("task")
            project = serializer.validated_data.get("project")

            if task:
                if not task.project.team_members.filter(id=request.user.id).exists():
                    return Response(
                        {"message": "You are not a member of this project."},
                        status=status.HTTP_403_FORBIDDEN,
                    )

            if project:
                if not project.team_members.filter(id=request.user.id).exists():
                    return Response(
                        {"message": "You are not a member of this project."},
                        status=status.HTTP_403_FORBIDDEN,
                    )

            comment = serializer.save(author=request.user)

            return Response(
                CommentSerializer(comment).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class CommentDetailView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, comment_id):
        comment = get_object_or_none(Comment, comment_id)

        if comment is None:
            return Response(
                {"message": "Comment not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        self.check_object_permissions(request, comment)

        serializer = CommentSerializer(comment)

        return Response(serializer.data)

    def put(self, request, comment_id):
        comment = get_object_or_none(Comment, comment_id)

        if comment is None:
            return Response(
                {"message": "Comment not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        self.check_object_permissions(request, comment)

        serializer = CommentSerializer(
            comment,
            data=request.data,
        )

        if serializer.is_valid():
            updated_comment = serializer.save()

            return Response(
                CommentSerializer(updated_comment).data,
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, comment_id):
        comment = get_object_or_none(Comment, comment_id)

        if comment is None:
            return Response(
                {"message": "Comment not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        self.check_object_permissions(request, comment)

        comment.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )
