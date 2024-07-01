from rest_framework import serializers

from core.models import City, Country, SocialMedia


class CountrySerializer(serializers.ModelSerializer):
    """Сериализатор для страны."""
    class Meta:
        fields = ('id', 'name')
        model = Country


class CitySerializer(serializers.ModelSerializer):
    """Сериализатор для города."""
    country = CountrySerializer(read_only=True)
    class Meta:
        fields = ('id', 'name', 'country')
        model = City


class SocialMediaSerializer(serializers.ModelSerializer):
    """Сериализатор для списка социальных сетей."""
    class Meta:
        fields = ('id', 'name')
        model = SocialMedia
