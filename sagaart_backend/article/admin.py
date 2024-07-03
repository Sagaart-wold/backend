from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'briefe',
                    'created_at',
                    'thumbnail',
                    'city')

    list_filter = ('created_at', 'city')
    search_fields = ('briefe', 'text')
    ordering = ['-created_at']
