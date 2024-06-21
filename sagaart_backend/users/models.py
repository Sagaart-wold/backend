from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, user_id, first_name, last_name, phone_number, password=None, subscription_id=None, order_id=None, favourite_artist_id=None, favourite_art_obj_id=None):
        if not user_id:
            raise ValueError('У пользователей должен быть user_id')
        user = self.model(
            user_id=user_id,
            user_first_name=first_name,
            user_last_name=last_name,
            user_phone_number=phone_number,
            subscription_id=subscription_id,
            order_id=order_id,
            favourite_artist_id=favourite_artist_id,
            favourite_art_obj_id=favourite_art_obj_id
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, first_name, last_name, phone_number, password=None, subscription_id=None, order_id=None, favourite_artist_id=None, favourite_art_obj_id=None):
        user = self.create_user(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            password=password,
            subscription_id=subscription_id,
            order_id=order_id,
            favourite_artist_id=favourite_artist_id,
            favourite_art_obj_id=favourite_art_obj_id
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_id = models.IntegerField(primary_key=True)
    user_first_name = models.CharField(max_length=30)
    user_last_name = models.CharField(max_length=30)
    user_phone_number = models.IntegerField()
    password = models.CharField(max_length=128)
    subscription_id = models.ForeignKey('Subscription', on_delete=models.CASCADE)
    order_id = models.ForeignKey('Order', on_delete=models.SET_NULL)
    favourite_artist_id = models.ForeignKey('Artist', on_delete=models.SET_NULL)
    favourite_art_obj_id = models.ForeignKey('ArtObject', on_delete=models.SET_NULL)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['user_first_name', 'user_last_name', 'user_phone_number', 'subscription_id', 'order_id', 'favourite_artist_id', 'favourite_art_obj_id']

    def get_username(self):
        return str(self.user_id)

    def get_full_name(self):
        return f"{self.user_first_name} {self.user_last_name}"

    def __str__(self):
        return self.get_full_name()


class Subscription(models.Model):
    subscription_id =


class Order(models.Model):
    order_id = 


class Artist(models.Model):
    artist_id = 


class ArtObject(models.Model):
    art_obj_id = 
