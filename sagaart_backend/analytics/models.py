from datetime import date

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

from core.models import ABSModelWithUniqueName
from core.constants import MAX_LENGTH_CHARFIELD, MAX_LENGTH_TEXTFIELD

User = get_user_model()


class Subscription(models.Model):
    """Model Subscription."""

    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_LENGTH_CHARFIELD,
    )
    price = models.DecimalField(
        verbose_name="Стоимость",
        max_digits=10,
        decimal_places=2,
    )
    info = models.TextField(
        verbose_name='Описание',
        max_length=MAX_LENGTH_TEXTFIELD,
    )
    period = models.SmallIntegerField(
        verbose_name="Период подписки в днях",
    )
    is_actual = models.BooleanField(
        verbose_name="Действующий тариф",
        default=True
    )

    class Meta:
        verbose_name = "Вид подписки"
        verbose_name_plural = "Виды подписок"

    def __str__(self):
        return f'{self.name}'


class UserSubscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='ID пользователя',
    )
    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.CASCADE,
        verbose_name='ID подписки',
    )
    created_at = models.DateField(
        verbose_name='Дата начала подписки',
        validators = [
            MaxValueValidator(
                limit_value=date.today,
            )
        ],
        auto_now_add = date.today()
    )
    ended_at = models.DateField(
    #  Вычислить дату окончания, в зависимости от начала подписки и периода
        verbose_name='Дата начала подписки',
    )

    class Meta:
        verbose_name = "Подписка пользователя"
        verbose_name_plural = "Подписки пользователя"
        default_related_name = 'user_subscriptions'

    def __str__(self):
        return f'{self.user} -> {self.subscription}'
