import logging

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment
from .serializers import CommentSerializer

logger = logging.getLogger(__name__)


class CommentListCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        comments = Comment.objects.all()

        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            comment = serializer.save()

            logger.info("Comment created: %s", comment.id)

            return Response(
                CommentSerializer(comment).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)

        serializer = CommentSerializer(comment)

        return Response(serializer.data)

    def put(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)

        serializer = CommentSerializer(comment, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)

        logger.info("Comment deleted: %s", comment.id)

        comment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
