from django.contrib import admin
from .models import ShoppingCart
from artobjects.models import ArtObject


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'status']
    # inlines = (ArtObjectInline,)
    raw_id_fields = ['user',]
    filter_horizontal=('artobjects',)


