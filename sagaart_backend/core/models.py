from django.db import models

from .constants import MAX_LENGTH_CHARFIELD
# Файл с константами предлагаю оставить в core

class Country(models.Model):
    """Model Country."""
    name = models.CharField(
        max_length=MAX_LENGTH_CHARFIELD,
        blank=False,
        verbose_name="Название страны",
        help_text="Введите название страны",
        unique=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    """Model City."""
    name = models.CharField(
        max_length=MAX_LENGTH_CHARFIELD,
        blank=False,
        verbose_name="Название города",
        help_text="Введите название города",
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        blank=False,
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


class Images(models.Model):
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
        blank=False,
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


class SocialMedia(models.Model):
    """Model SocialMedia."""
    name = models.CharField(
        max_length=MAX_LENGTH_CHARFIELD,
        blank=False,
        verbose_name="Название социальной сети",
        help_text="Введите название социальной сети",
        unique=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return f'{self.name}'
