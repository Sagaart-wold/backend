from datetime import date

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

from .constants import MAX_LENGTH_CHARFIELD, MAX_LENGTH_TEXTFIELD

User = get_user_model()


class Category(models.Model):
    """Model Category."""
    name = models.CharField(
        max_length=MAX_LENGTH_CHARFIELD,
        verbose_name="Название категории",
        help_text="Введите название категории",
        unique=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f'{self.name}'


class Color(models.Model):
    """Model Color."""
    name = models.CharField(
        max_length=MAX_LENGTH_CHARFIELD,
        verbose_name="Название цветовой палитры",
        help_text="Введите название цветовой палитры",
        unique=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Цветовая палитра"
        verbose_name_plural = "цветовые палитры"

    def __str__(self):
        return f'{self.name}'


class Genre(models.Model):
    """Model Genre."""
    name = models.CharField(
        max_length=MAX_LENGTH_CHARFIELD,
        verbose_name="Название жанра",
        help_text="Введите название жанра",
        unique=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Жанра"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return f'{self.name}'


class MaterialArtObject(models.Model):
    """Model MaterialArtObject."""
    name = models.CharField(
        max_length=MAX_LENGTH_CHARFIELD,
        verbose_name="Название материала арт объекта",
        help_text="Введите название материала арт объекта",
        unique=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Материал арт объекта"
        verbose_name_plural = "материалы арт объекта"

    def __str__(self):
        return f'{self.name}'


class BaseArtObject(models.Model):
    """Model BaseArtObject."""
    name = models.CharField(
        max_length=MAX_LENGTH_CHARFIELD,
        verbose_name="Название основы арт объекта",
        help_text="Введите название основы арт объекта",
        unique=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Основа арт объекта"
        verbose_name_plural = "Основы арт объекта"

    def __str__(self):
        return f'{self.name}'



class Style(models.Model):
    """Model Style."""
    name = models.CharField(
        max_length=MAX_LENGTH_CHARFIELD,
        verbose_name="Название стиля",
        help_text="Введите название стиля",
        unique=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Стиль"
        verbose_name_plural = "Стили"

    def __str__(self):
        return f'{self.name}'


class Artist(models.Model):
    class Sex(models.IntegerChoices):
        MALE = 1, 'М'
        FEMALE = 2, 'Ж'

    first_name = models.CharField(
        verbose_name="Имя",
        max_length=MAX_LENGTH_CHARFIELD,
    )
    last_name = models.CharField(
        verbose_name="Имя",
        max_length=MAX_LENGTH_CHARFIELD,
    )
    description = models.TextField(
        verbose_name="О художнике",
        blank=True,
        max_length=MAX_LENGTH_TEXTFIELD,
    )
    sex = models.PositiveSmallIntegerField(
        verbose_name="Пол",
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


class ABSModelWithArtistField(models.Model):
    artist = models.ForeignKey(
        'Artist',
        verbose_name='Художник',
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class ArtistSocialMedia(ABSModelWithArtistField):
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
        default_related_name = "social_medias"


class TeachingActivities(ABSModelWithArtistField):
    educational_institutions = models.ForeignKey(
        'EducationalInstitution',
        verbose_name='Учреждение',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    started_at = models.DateField(
        verbose_name="Начало",
        validators=[
            MaxValueValidator(
                limit_value=date.today,
            )
        ],
    )
    ended_at = models.DateField(
        verbose_name="Конец",
        validators=[
            MaxValueValidator(
                limit_value=date.today,
            )
        ],
    )

    class Meta:
        verbose_name = "Преподавание"
        verbose_name_plural = "Преподавание"
        default_related_name = "teaching"


class Education(TeachingActivities):
    degree = models.CharField(
        verbose_name="Степень",
        max_length=MAX_LENGTH_CHARFIELD,
    )

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образование"
        default_related_name = "education"


class EducationalInstitution(models.Model):
    class TypeEducationalInstitution(models.IntegerChoices):
        UNIVERSITY = 1, 'Университет'
        COLLEGE = 2, 'Колледж'
        ART_SCHOOL = 3, 'Школа искусств'
        COURSES = 4, 'Курсы'

    name = models.CharField(
        verbose_name="Название",
        max_length=MAX_LENGTH_CHARFIELD,
    )
    type_ei = models.PositiveSmallIntegerField(
        verbose_name="Тип учебного заведения",
        choices=TypeEducationalInstitution.choices,
        blank=True,
    )
    city_of_birth = models.ForeignKey(
        'core.City',
        verbose_name="Город",
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Учебное заведение"
        verbose_name_plural = "Учебные Заведения"
        default_related_name = "educational_institution"


class ArtistAward(ABSModelWithArtistField):
    award = models.ForeignKey(
        'Award',
        verbose_name='Награда',
        on_delete=models.CASCADE,
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год',
        validators=[
            MaxValueValidator(
                limit_value=date.today().year,
            )
        ],
    )
    city = models.ForeignKey(
        'core.City',
        verbose_name="Город",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"
        default_related_name = "artist_awards"


class Award(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=MAX_LENGTH_CHARFIELD,
    )
