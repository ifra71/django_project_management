from rest_framework import serializers

from .models import Profile, User


class UserSerializer(serializers.ModelSerializer):

    role = serializers.CharField()
    contact_number = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ["id", "email", "password", "role", "contact_number"]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):

        role = validated_data["role"]
        contact_number = validated_data.get("contact_number", "")

        user = User.objects.create_user(
            email=validated_data["email"], password=validated_data["password"]
        )

        Profile.objects.create(user=user, role=role, contact_number=contact_number)

        return user


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()
