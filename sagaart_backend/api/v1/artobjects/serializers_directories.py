from rest_framework import serializers

from artobjects.models import (Award, BaseArtObject, Category, Color, Genre,
                               MaterialArtObject, Style)


class AwardSerializer(serializers.ModelSerializer):
    """Cериализатор для списка наград."""
    class Meta:
        fields = ('id', 'name')
        model = Award


class BaseArtObjectSerializer(serializers.ModelSerializer):
    """Cериализатор для списка основ для произведений искусств."""
    class Meta:
        fields = ('id', 'name')
        model = BaseArtObject


class CategorySerializer(serializers.ModelSerializer):
    """Cериализатор для списка категорий."""
    class Meta:
        fields = ('id', 'name')
        model = Category


class ColorSerializer(serializers.ModelSerializer):
    """Cериализатор для списка цветовых гамм."""

    class Meta:
        fields = ('id', 'name')
        model = Color


class GenreSerializer(serializers.ModelSerializer):
    """Cериализатор для списка жанров."""

    class Meta:
        fields = ('id', 'name')
        model = Genre


class MaterialArtObjectSerializer(serializers.ModelSerializer):
    """Cериализатор для списка материалов, с помощью которых написано
     произведений искусств."""

    class Meta:
        fields = ('id', 'name')
        model = MaterialArtObject


class StyleSerializer(serializers.ModelSerializer):
    """Cериализатор для списка стилей."""

    class Meta:
        fields = ('id', 'name')
        model = Style
