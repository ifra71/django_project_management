from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("email required")

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )

    ROLE_CHOICES = [
        ("manager", "Manager"),
        ("qa", "QA"),
        ("developer", "Developer"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    contact_number = models.CharField(max_length=20, blank=True)
