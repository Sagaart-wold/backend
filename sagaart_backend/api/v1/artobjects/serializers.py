from django.contrib.auth import get_user_model
from rest_framework import serializers

from artobjects.models import Artist, ArtistAward, ArtObject, Education, Show


User = get_user_model()


class BaseArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = (
            "id",
            "first_name",
            "last_name",
            "description",
            "sex",
            "date_of_birth",
            "date_of_death",
            "personal_style",
            "city_of_birth",
            "city_of_living",
            "personal_style",
            "photo",
        )
        depth = 2


class BaseArtObjectsShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtObject
        fields = [
            'id',
            'vendor',
            'name',
            'status',
            'category',
            'colors',
            'genre',
            'width',
            'height',
            'material_art_object',
            'base_art_object',
            'style',
            'main_image',
            'orientation',
            'tag_size',
            'actual_price',
        ]
        depth = 3


class ArtistWriteSerializer(BaseArtistSerializer):
    class Meta(BaseArtistSerializer.Meta):
        pass


class ShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Show
        fields = ['name', 'started_at', 'ended_at', 'place', 'personal']
        depth = 3


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'address']


class ArtObjectListSerializer(serializers.ModelSerializer):
    """Cериализатор для списка артобъектов (list)"""
    tag_size = serializers.SerializerMethodField(read_only=True)
    orientation = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)
    is_favourite = serializers.SerializerMethodField(read_only=True)
    artist = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ArtObject
        fields = [
            'id',
            'artist',
            'vendor',
            'name',
            'status',
            'category',
            'colors',
            'genre',
            'width',
            'height',
            'material_art_object',
            'base_art_object',
            'style',
            'main_image',
            'is_favourite',
            'orientation',
            'tag_size',
            'actual_price',
        ]
        depth = 3

    def get_status(self, instance):
        return instance.get_status_display()

    def get_orientation(self, instance):
        return instance.get_orientation_display()

    def get_tag_size(self, instance):
        return instance.get_tag_size_display()

    def get_is_favourite(self, instance):
        user = self.context["request"].user
        return (
            user.is_authenticated and instance.favorited_by.filter(id=user.pk).exists()
        )

    def get_artist(self, instance):
        artist = {}
        artist['id'] = instance.artist.id
        artist['first_name'] = instance.artist.first_name
        artist['last_name'] = instance.artist.last_name
        return artist


class ArtObjectRetrieveSerializer(ArtObjectListSerializer):
    """Cериализатор для артобъекта (retrieve)"""
    owner = OwnerSerializer(read_only=True)
    shows = ShowSerializer(many=True, read_only=True)
    artist = BaseArtistSerializer(read_only=True)

    class Meta:
        fields = [
            'id',
            'owner',
            'artist',
            'vendor',
            'name',
            'date_of_creation',
            'status',
            'city_sold',
            'category',
            'colors',
            'genre',
            'width',
            'height',
            'material_art_object',
            'base_art_object',
            'style',
            'collection',
            'unique',
            'art_investment',
            'images',
            'main_image',
            'max_amount',
            'is_favourite',
            'orientation',
            'tag_size',
            'actual_price',
            'shows',
        ]
        model = ArtObject
        depth = 3


class ArtistReadListSerializer(BaseArtistSerializer):
    is_favorite = serializers.SerializerMethodField(read_only=True)
    artobjects = serializers.SerializerMethodField(read_only=True)

    class Meta(BaseArtistSerializer.Meta):
        fields = (
            "id",
            "first_name",
            "last_name",
            "city_of_living",
            "artobjects",
            "is_favorite",
            "photo",
        )
        read_only_fields = fields

    def get_is_favorite(self, instance):
        user = self.context["request"].user
        return (
            user.is_authenticated and instance.favorited_by.filter(id=user.pk).exists()
        )

    def get_sex(self, instance):
        return instance.get_sex_display()

    def get_artobjects(self, instance):
        artobject = instance.artobjects.first()
        return BaseArtObjectsShortSerializer(artobject).data


class AristAwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistAward
        fields = ('award', 'year', 'city',)
        depth = 2


class AristEducationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('degree', 'ended_at', 'educational_institutions')
        depth = 1


class ArtistReadRetrieveSerializer(ArtistReadListSerializer):
    is_favorite = serializers.SerializerMethodField(read_only=True)
    artobjects = BaseArtObjectsShortSerializer(many=True)
    shows = serializers.SerializerMethodField(read_only=True)
    awards = serializers.SerializerMethodField(read_only=True)
    education = serializers.SerializerMethodField(read_only=True)

    class Meta(BaseArtistSerializer.Meta):
        fields = BaseArtistSerializer.Meta.fields + (
            'artobjects',
            "is_favorite",
            "shows",
            'awards',
            'education'
        )
        read_only_fields = fields

    def get_is_favorite(self, instance):
        user = self.context["request"].user
        return (
            user.is_authenticated and instance.favorited_by.filter(id=user.pk).exists()
        )

    def get_shows(self, instance):
        shows = Show.objects.filter(
            artobjects__in=instance.artobjects.all()
        ).distinct()
        serializer = ShowSerializer(shows, many=True)
        return serializer.data

    def get_awards(self, instance):
        awards = instance.artist_awards.all()
        serializer = AristAwardsSerializer(awards, many=True)
        return serializer.data

    def get_education(self, instance):
        education = Education.objects.filter(artist=instance)  # Двойное наследование теряет обратную связь
        serializer = AristEducationsSerializer(education, many=True)
        return serializer.data