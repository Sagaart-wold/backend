from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, first_name='', last_name='', **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Поле пароля
    roles = models.CharField(max_length=255, blank=True, null=True)  # Роли пользователя
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Дата создания аккаунта
    first_name = models.CharField(max_length=30)  # Имя пользователя
    last_name = models.CharField(max_length=30)  # Фамилия пользователя
    phone = models.CharField(max_length=15, blank=True, null=True)  # Номер телефона
    address = models.TextField(blank=True)  # Адрес пользователя

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email

