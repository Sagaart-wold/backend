from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum


class UserRole(Enum):
    ADMIN = 'admin'
    USER = 'user'
    SELLER = 'seller'


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    role = models.CharField(
        choices=[(role.value, role.name) for role in UserRole],
        default=UserRole.USER.value,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
