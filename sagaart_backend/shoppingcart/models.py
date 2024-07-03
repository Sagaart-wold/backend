from datetime import date

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

from core.constants import MAX_LENGTH_CHARFIELD, MAX_LENGTH_TEXTFIELD
from artobjects.models import ArtObject

User = get_user_model()


class ShoppingCart(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Покупатель',
    )
    artobject = models.ForeignKey(
        ArtObject,
        on_delete=models.CASCADE,
        verbose_name='Артобъект'
    )
    #Заглушка, пока только в 1 экземпляре
    amount = models.PositiveIntegerField(
        verbose_name='Количество',
        default=1
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'artobject'],
                name='cart_user_artobject'
            )
        ]
        verbose_name = "Покупка пользователя"
        verbose_name_plural = "Покупки пользователя"
        default_related_name = 'shopping_cart'



