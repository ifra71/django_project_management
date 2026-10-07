import logging

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProfileSerializer, RegisterSerializer

logger = logging.getLogger(__name__)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            logger.info("New user registered: %s", user.email)

            return Response(
                {
                    "message": "User registered successfully.",
                    "user": {
                        "id": user.id,
                        "name": user.name,
                        "email": user.email,
                    },
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class ProfileView(APIView):
    def get(self, request):
        profile = request.user.profile
        return Response(
            ProfileSerializer(profile).data,
            status=status.HTTP_200_OK,
        )

    def put(self, request):
        profile = request.user.profile
        serializer = ProfileSerializer(
            profile,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
