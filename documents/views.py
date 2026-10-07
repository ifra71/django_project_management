from rest_framework import generics, mixins

from common.permissions import IsProjectMemberOrReadOnly

from .models import Document
from .serializers import DocumentSerializer


class DocumentListCreateView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class DocumentDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsProjectMemberOrReadOnly]
    lookup_url_kwarg = "document_id"

    def get(self, request, document_id):
        return self.retrieve(request)

    def put(self, request, document_id):
        return self.update(request)

    def delete(self, request, document_id):
        return self.destroy(request)
