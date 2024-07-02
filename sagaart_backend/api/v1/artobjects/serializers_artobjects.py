# from django.contrib.auth import get_user_model
# from rest_framework import serializers
#
# from .serializers import ArtistReadSerializer
#
#
#
# class ShowSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Show
#         fields = ['name', 'started_at', 'ended_at', 'place', 'personal']
#         depth = 3
#
#
# class OwnerSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'address']
#
#
# class ArtObjectListSerializer(serializers.ModelSerializer):
#     """Cериализатор для списка артобъектов (list)"""
#     tag_size = serializers.SerializerMethodField(read_only=True)
#     orientation = serializers.SerializerMethodField(read_only=True)
#     status = serializers.SerializerMethodField(read_only=True)
#     is_favourite =serializers.SerializerMethodField(read_only=True)
#     artist = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = ArtObject
#         fields = [
#             'id',
#             'artist',
#             'vendor',
#             'name',
#             'status',
#             'category',
#             'colors',
#             'genre',
#             'width',
#             'height',
#             'material_art_object',
#             'base_art_object',
#             'style',
#             'main_image',
#             'is_favourite',
#             'orientation',
#             'tag_size',
#             'actual_price',
#         ]
#         depth = 3
#
#     def get_status(self, instance):
#         return instance.get_status_display()
#
#     def get_orientation(self, instance):
#         return instance.get_orientation_display()
#
#     def get_tag_size(self, instance):
#         return instance.get_tag_size_display()
#
#     def get_is_favourite(self, instance):
#         user = self.context["request"].user
#         return (
#             user.is_authenticated and instance.favorited_by.filter(id=user.pk).exists()
#         )
#
#     def get_artist(self, instance):
#         artist = {}
#         artist['id'] = instance.artist.id
#         artist['first_name'] = instance.artist.first_name
#         artist['last_name'] = instance.artist.last_name
#         return artist
#
#
# class ArtObjectRetrieveSerializer(ArtObjectListSerializer):
#     """Cериализатор для артобъекта (retrieve)"""
#     owner = OwnerSerializer(read_only=True)
#     shows = ShowSerializer(many=True, read_only=True)
#     artist = ArtistReadSerializer(read_only=True)
#
#     class Meta:
#         fields = [
#             'id',
#             'owner',
#             'artist',
#             'vendor',
#             'name',
#             'date_of_creation',
#             'status',
#             'city_sold',
#             'category',
#             'colors',
#             'genre',
#             'width',
#             'height',
#             'material_art_object',
#             'base_art_object',
#             'style',
#             'collection',
#             'unique',
#             'art_investment',
#             'images',
#             'main_image',
#             'max_amount',
#             'is_favourite',
#             'orientation',
#             'tag_size',
#             'actual_price',
#             'shows',
#         ]
#         model = ArtObject
#         depth = 3
