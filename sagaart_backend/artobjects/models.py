from datetime import date

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

from .constants import MAX_LENGTH_CHARFIELD, MAX_LENGTH_TEXTFIELD

User = get_user_model()


class Artist(models.Model):
    class Sex(models.IntegerChoices):
        MALE = 1, 'male'
        FEMALE = 2, 'female'

    first_name = models.CharField(
        verbose_name="Имя",
        max_length=MAX_LENGTH_CHARFIELD,
        blank=False,
    )
    last_name = models.CharField(
        verbose_name="Имя",
        max_length=MAX_LENGTH_CHARFIELD,
        blank=False,
    )
    description = models.TextField(
        verbose_name="О художнике",
        blank=True,
        max_length=MAX_LENGTH_TEXTFIELD,
    )
    sex = models.PositiveSmallIntegerField(
        verbose_name="Видимость",
        choices=Sex.choices,
        blank=True,
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения",
        validators=[
            MaxValueValidator(
                limit_value=date.today,
            )
        ],
        null=True,
        blank=True,
    )
    date_of_death = models.DateField(  # В сериализаторе поле не должно отображаться если пустое!
        verbose_name="Дата смерти",
        validators=[
            MaxValueValidator(
                limit_value=date.today,
            )
        ],
        null=True,
        blank=True,
        default=None,
    )
    city_of_birth = models.ForeignKey(
        'core.City',
        verbose_name="Город рождения",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    city_of_living = models.ForeignKey(
        'core.City',
        verbose_name="Город проживания",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    personal_style = models.BooleanField(
        verbose_name="Персональный стиль",
        default=False
    )
    photo = models.ForeignKey(
        'core.Image',
        verbose_name='Фото художника',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    favorited_by = models.ManyToManyField(
        to=User,
        blank=True,
        verbose_name="Добавили в избранное",
        related_name="favorite_artists",
    )

    class Meta:
        verbose_name = "Художник"
        verbose_name_plural = "Художники"
        ordering = ("last_name", "first_name")
        default_related_name = "artists"


class ArtistSocialMedia(models.Model):
    artist = models.ForeignKey(
        'Artist',
        verbose_name='Художник',
        on_delete=models.CASCADE,
    )
    link = models.URLField(
        verbose_name='Ссылка',
        unique=True,
    )
    social_media = models.ForeignKey(
        'core.SocialMedia',
        verbose_name='Социальная сеть',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Художник"
        verbose_name_plural = "Художники"
        default_related_name = "artist_social_medias"
