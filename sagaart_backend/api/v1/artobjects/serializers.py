from rest_framework import serializers

from artobjects.models import Artist


class ArtistWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class ArtistReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"
        read_only_fields = fields

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if not ret.get('date_of_death', None):  # Удаляем поле дата смерти, если оно пустое
            ret.pop('date_of_death')
        return ret
