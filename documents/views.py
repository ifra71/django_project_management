import logging

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Document
from .serializers import DocumentSerializer

logger = logging.getLogger(__name__)


class DocumentListCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        documents = Document.objects.all()

        serializer = DocumentSerializer(documents, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = DocumentSerializer(data=request.data)

        if serializer.is_valid():
            document = serializer.save()

            logger.info("Document created: %s", document.name)

            return Response(
                DocumentSerializer(document).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, document_id):
        document = Document.objects.get(id=document_id)

        serializer = DocumentSerializer(document)

        return Response(serializer.data)

    def put(self, request, document_id):
        document = Document.objects.get(id=document_id)

        serializer = DocumentSerializer(document, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, document_id):
        document = Document.objects.get(id=document_id)

        logger.info("Document deleted: %s", document.name)

        document.delete()

        return Response(
            {"message": "document deleted"}, status=status.HTTP_204_NO_CONTENT
        )
