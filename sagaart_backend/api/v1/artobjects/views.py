from rest_framework import viewsets, permissions

from artobjects.models import Artist

from .serializers import ArtistWriteSerializer, ArtistReadSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch']

    def get_queryset(self):
        return Artist.objects.select_related(
            'city_of_birth',
            'city_of_living',
            'photo'
        ).prefect_related(
            'favorited_by'
        )

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ArtistReadSerializer
        if self.request.user.is_staff:
            return ArtistWriteSerializer
