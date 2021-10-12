from django.db import models
from django.contrib.auth.models import AbstractUser

USER_ROLES = [
    ('u', 'user'),
    ('m', 'moderator'),
    ('a', 'admin'),]

class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,)
    role = models.CharField(max_length=1, choices=USER_ROLES, blank=True)


