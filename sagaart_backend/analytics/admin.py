from django.contrib import admin
from .models import Subscription, UserSubscription


@admin.register(Subscription)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'info', 'period', 'is_actual']
    search_fields = ['name']


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'subscription', 'created_at', 'ended_at']

    search_fields = ['user']
    list_filter = ['user', 'subscription']

    raw_id_fields = ['user', 'subscription']
