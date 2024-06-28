from datetime import date

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

from core.models import ABSModelWithUniqueName
from .constants import MAX_LENGTH_CHARFIELD, MAX_LENGTH_TEXTFIELD

User = get_user_model()


class Category(ABSModelWithUniqueName):
    """Model Category."""

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f'{self.name}'


class Color(ABSModelWithUniqueName):
    """Model Color."""

    class Meta:
        verbose_name = "Цветовая палитра"
        verbose_name_plural = "цветовые палитры"

    def __str__(self):
        return f'{self.name}'


class Genre(ABSModelWithUniqueName):
    """Model Genre."""

    class Meta:
        verbose_name = "Жанра"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return f'{self.name}'


class MaterialArtObject(ABSModelWithUniqueName):
    """Model MaterialArtObject."""

    class Meta:
        verbose_name = "Материал арт объекта"
        verbose_name_plural = "материалы арт объекта"

    def __str__(self):
        return f'{self.name}'


class BaseArtObject(ABSModelWithUniqueName):
    """Model BaseArtObject."""

    class Meta:
        verbose_name = "Основа арт объекта"
        verbose_name_plural = "Основы арт объекта"

    def __str__(self):
        return f'{self.name}'


class Style(ABSModelWithUniqueName):
    """Model Style."""

    class Meta:
        verbose_name = "Стиль"
        verbose_name_plural = "Стили"

    def __str__(self):
        return f'{self.name}'


class Artist(models.Model):
    """Model Artist."""
    class Sex(models.IntegerChoices):
        MALE = 1, 'М'
        FEMALE = 2, 'Ж'

    first_name = models.CharField(
        verbose_name="Имя",
        max_length=MAX_LENGTH_CHARFIELD,
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
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
        related_name='city_of_birth'
    )
    city_of_living = models.ForeignKey(
        'core.City',
        verbose_name="Город проживания",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='city_of_living'

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
    )

    class Meta:
        verbose_name = "Художник"
        verbose_name_plural = "Художники"
        ordering = ("last_name", "first_name")
        default_related_name = "artists"


class ABSModelWithArtistField(models.Model):
    """Абстрактная модель. Добавляет связь с художником."""
    artist = models.ForeignKey(
        'Artist',
        verbose_name='Художник',
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class ArtistSocialMedia(ABSModelWithArtistField):
    """Model ArtistSocialMedia."""
    link = models.URLField(
        verbose_name='Ссылка на аккаунт',
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
        verbose_name = "Социальная сеть художника"
        verbose_name_plural = "Социальные сеть художника"
        default_related_name = "social_medias"


class TeachingActivities(ABSModelWithArtistField):
    """Model TeachingActivities."""
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
    """Model Education."""
    degree = models.CharField(
        verbose_name="Степень",
        max_length=MAX_LENGTH_CHARFIELD,
    )

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образование"
        default_related_name = "education"


class EducationalInstitution(models.Model):
    """Model EducationalInstitution."""
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
    """Model ArtistAward."""
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
        verbose_name = "Награда художника"
        verbose_name_plural = "Награды художника"
        default_related_name = "artist_awards"


class Award(ABSModelWithUniqueName):

    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"

    def __str__(self):
        return f'{self.name}'


class Collection(ABSModelWithUniqueName):
    """Model Collection."""
    created_at = models.DateField(
        verbose_name="Дата создания коллекции",
        validators=[
            MaxValueValidator(
                limit_value=date.today,
            )
        ],
        null=True,
        blank=True,
    )
    private = models.BooleanField(
        verbose_name="Частная коллекция",
        default=False,
    )

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"

    def __str__(self):
        return f'{self.name}'


class ArtObject(ABSModelWithArtistField):
    """Model ArtObject."""
    class SaleStatus(models.IntegerChoices):
        ONSALE = 1, 'В продаже'
        SOLD = 2, 'Продана'
        NOTFORSALE = 3, 'Не продается'

    class Orientation(models.IntegerChoices):
        HORIZONTAL = 1, 'Горизонтальная'
        VERTICAL = 2, 'Вертикальная'

    class TagSize(models.IntegerChoices):
        SMALL = 1, 'до 40 см'
        MEDIUM = 2, '40 - 100 см'
        LARGE = 3, '100 - 160 см'
        OVERSIZE = 4, 'более 160 см'

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner',
        verbose_name='ID пользователя',
    )
    vendor = models.IntegerField(
        verbose_name='Артикул',
        unique=True,
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_LENGTH_CHARFIELD,
    )
    date_of_creation = models.DateField(
        verbose_name='Дата создания'
    )
    status = models.PositiveSmallIntegerField(
        verbose_name="Статус объекта",
        choices=SaleStatus.choices,
        default=SaleStatus.choices[2],
    )
    city_sold = models.ForeignKey(
        'core.City',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='city_sold',
        verbose_name='ID города',
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='ID категории',
    )
    colors = models.ManyToManyField(
        'Color',
        verbose_name='Цветовая гамма',
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name='ID жанра',
    )
    width = models.PositiveIntegerField(
        verbose_name='Ширина объекта'
    )
    height = models.PositiveIntegerField(
        verbose_name='Высота объекта'
    )
    material_art_object = models.ForeignKey(
        'MaterialArtObject',
        on_delete=models.CASCADE,
        related_name='material',
        verbose_name='Материал',
    )
    base_art_object = models.ForeignKey(
        'BaseArtObject',
        on_delete=models.CASCADE,
        related_name='base',
        verbose_name='Основа',
    )
    style = models.ForeignKey(
        'Style',
        on_delete=models.CASCADE,
        verbose_name='Стиль',
    )
    collection = models.ForeignKey(
        'Collection',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='В коллекции',
    )
    unique = models.BooleanField(
        default=False,
        verbose_name='Уникальная работа',
    )
    art_investment = models.BooleanField(
        default=False,
        verbose_name='Вклад в искусство',
    )
    images = models.ManyToManyField(
        'core.Image',
        blank=True,
        related_name='images',
        verbose_name='Изображения объекта',
    )
    main_image = models.OneToOneField(
        'core.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='main_image',
        verbose_name='Изображения объекта',
    )
    max_amount = models.IntegerField(
        default=1,
        verbose_name='Количество объектов в продаже',
    )
    favourited_by = models.ManyToManyField(
        User,
        verbose_name='ID пользователя',
    )
    orientation = models.PositiveSmallIntegerField(  # При сохранении вычисляется
        verbose_name="Ориентация",
        choices=Orientation.choices,
        blank=True,
    )
    tag_size = models.PositiveSmallIntegerField(  # При сохранении вычисляется
        verbose_name="Тег размера",
        choices=TagSize.choices,
        blank=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Артобъект"
        verbose_name_plural = "Артобъекты"

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.orientation = 1 if (self.width > self.height) else 2
        bigger = max((self.width, self.height), key=lambda i: int(i))
        if bigger <= 40:
            tag_size = self.TagSize.choices[1]
        elif bigger <= 100:
            tag_size = self.TagSize.choices[2]
        elif bigger <= 160:
            tag_size = self.TagSize.choices[3]
        else: tag_size = self.TagSize.choices[4]
        self.tag_size = tag_size
        super().save(*args, **kwargs)


class ABSModelWithArtObjectField(models.Model):

    artobject = models.ForeignKey(
        'ArtObject',
        verbose_name='Арт объект',
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class Gallery(models.Model):
    """Model Gallery."""
    name = models.CharField(
        verbose_name="Название",
        max_length=MAX_LENGTH_CHARFIELD,
    )
    city = models.ForeignKey(
        'core.City',
        verbose_name="Город",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"

    def __str__(self):
        return f'{self.name}'


class Show(ABSModelWithArtObjectField):
    """Model Show."""
    name = models.CharField(
        verbose_name="Название",
        max_length=MAX_LENGTH_CHARFIELD,
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
    place = models.ForeignKey(
        'Gallery',
        on_delete=models.CASCADE,
        related_name='shows',
        verbose_name='ID галереи',
    )
    personal = models.BooleanField(
        verbose_name="Персональная",
        default=False,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Выставка"
        verbose_name_plural = "Выставки"

    def __str__(self):
        return f'{self.name}'


class Price(ABSModelWithArtObjectField):
    """Model Price."""
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2,
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        validators=[
            MaxValueValidator(
                limit_value=date.today,
            )
        ],
        auto_now_add=date.today()
    )

    class Meta:
        verbose_name = "Цена объекта"
        verbose_name_plural = "История цен объектов"
