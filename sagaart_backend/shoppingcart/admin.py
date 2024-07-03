from django.contrib import admin
from .models import ShoppingCart
from artobjects.models import ArtObject


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['user','artobject', 'amount']
    raw_id_fields = ['user','artobject',]


