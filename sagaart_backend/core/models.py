from django.db import models

from .constants import MAX_LENGTH_CHARFIELD
# Файл с константами предлагаю оставить в core


# core/models.py
from django.db import models


class ABSModelWithUniqueName(models.Model):
    """Абстрактная модель. Добавляет обязательное уникальное поле name."""
    name = models.CharField(
        max_length=MAX_LENGTH_CHARFIELD,
        verbose_name="Название",
        help_text="Введите название",
        unique=True,
    )

    class Meta:
        abstract = True
        ordering = ["name"]


class Country(ABSModelWithUniqueName):
    """Model Country."""

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    """Model City."""
    name = models.CharField(
        max_length=MAX_LENGTH_CHARFIELD,
        verbose_name="Название города",
        help_text="Введите название города",
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name="id страны",
        related_name='cities'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'country'],
                name='unique_city'
            )
        ]
        ordering = ["name"]
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return f'{self.name}'


class Image(models.Model):
    """Model Images."""
    name = models.CharField(
        max_length=MAX_LENGTH_CHARFIELD,
        blank=True,
        verbose_name="Название изображения",
        help_text="Введите название изображения",
        unique=True,
        null=True,
    )
    link = models.ImageField(
        upload_to='images/',
        help_text='Загрузите изображение',
        verbose_name='Изображение',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class SocialMedia(ABSModelWithUniqueName):
    """Model SocialMedia."""

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return f'{self.name}'
