from datetime import date

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

from core.constants import MAX_LENGTH_CHARFIELD, MAX_LENGTH_TEXTFIELD
from artobjects.models import ArtObject

User = get_user_model()


class ShoppingCart(models.Model):
    class ShoppingCartStatus(models.IntegerChoices):
        CART = 1, 'Корзина'
        DELIVERY = 2, 'Доставка'
        DONE = 3, 'Выполнен'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Покупатель',
    )
    # Пока каждый объект можно купить в одном экземпляре
    artobjects = models.ManyToManyField(
        ArtObject,
        blank=True,
        verbose_name='Артобъекты'
    )
    payment_at = models.DateField(
        verbose_name='Дата оплаты',
        validators=[
            MaxValueValidator(
                limit_value=date.today,
            )
        ],
        blank=True,
        null=True
    )
    address_delivery = models.TextField(
        max_length=MAX_LENGTH_TEXTFIELD,
        verbose_name='Адрес доставки',
        blank=True
    )
    status = models.PositiveSmallIntegerField(
        verbose_name="Статус объекта",
        choices=ShoppingCartStatus.choices,
        default=ShoppingCartStatus.choices[1],
    )
    is_payment = models.BooleanField(
        verbose_name='Оплата прошла',
        default=False
    )

    def save(self, *args, **kwargs):
        if self.is_payment:
            self.status = self.ShoppingCartStatus.choices[2]
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Покупка пользователя"
        verbose_name_plural = "Покупки пользователя"
        default_related_name = 'shoppingcarts'
        ordering = ['-payment_at']



