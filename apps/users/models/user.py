from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.users.managers.user_manager import MainUserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)

    objects = MainUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
