from rest_framework import serializers

from artobjects.models import Artist


class BaseArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = (
            'id',
            "first_name",
            "last_name",
            "description",
            "sex",
            "date_of_birth",
            "date_of_death",
            "personal_style",
            "city_of_birth",
            "city_of_living",
            "photo",
            "favorited_by"
        )


class ArtistWriteSerializer(BaseArtistSerializer):
    class Meta(BaseArtistSerializer.Meta):
        pass


class ArtistReadSerializer(BaseArtistSerializer):
    class Meta(BaseArtistSerializer.Meta):
        read_only_fields = BaseArtistSerializer.Meta.fields

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if not ret.get('date_of_death', None):  # Удаляем поле дата смерти, если оно пустое
            ret.pop('date_of_death')
        return ret
