from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    is_email_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=10)