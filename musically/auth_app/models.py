from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class AuthUser(AbstractUser):
    MAX_NAME_LEN = 35
    MAX_USERNAME_LEN = 30

    email = models.EmailField(
        unique=True,
    )

    username = models.CharField(
        unique=True,
        max_length=MAX_USERNAME_LEN
    )

    first_name = models.CharField(
        max_length=MAX_NAME_LEN,
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LEN,
    )

    profile_picture = models.ImageField()

    date_joined = models.DateTimeField(
        null=True,
        blank=True,
    )
