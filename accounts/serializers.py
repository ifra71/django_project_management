from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "profile_picture",
            "role",
            "contact_number",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    role = serializers.ChoiceField(
        choices=Profile.ROLE_CHOICES,
        required=False,
    )

    contact_number = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "password",
            "role",
            "contact_number",
        ]

    def create(self, validated_data):
        role = validated_data.get("role")
        contact_number = validated_data.get("contact_number")

        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            name=validated_data["name"],
        )

        profile = user.profile

        if role:
            profile.role = role

        if contact_number:
            profile.contact_number = contact_number

        profile.save()

        return user
