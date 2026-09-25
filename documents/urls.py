from django.urls import path

from .views import DocumentDetailView, DocumentListCreateView

urlpatterns = [
    path("documents/", DocumentListCreateView.as_view(), name="documents"),
    path(
        "documents/<int:document_id>/",
        DocumentDetailView.as_view(),
        name="document-detail",
    ),
]
