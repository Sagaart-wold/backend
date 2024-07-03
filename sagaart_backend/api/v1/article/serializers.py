from rest_framework import serializers
from core.models import City, Country, Image
from article.models import Article


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ['id', 'name', 'country']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'name', 'link', 'created_at']


class ArticleSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    thumbnail = ImageSerializer()

    class Meta:
        model = Article
        fields = '__all__'
