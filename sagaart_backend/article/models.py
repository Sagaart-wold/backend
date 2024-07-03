from django.db import models
from core.models import City, Image


class Article(models.Model):
    briefe = models.TextField(
        verbose_name="Краткое описание",
        help_text="Введите краткое описание статьи",
    )
    text = models.TextField(
        verbose_name="Текст статьи",
        help_text="Введите полный текст статьи",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    thumbnail = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Миниатюра",
        help_text="Выберите изображение для миниатюры статьи",
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Город",
        help_text="Выберите город, связанный со статьей",
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Article {self.id}"
