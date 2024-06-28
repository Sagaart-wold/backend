import logging

from rest_framework import generics, mixins

from artobjects.models import Artist
from rest_framework.viewsets import GenericViewSet

from .serializers import ArtistWriteSerializer, ArtistReadSerializer


class ArtistViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    serializer_class = ArtistReadSerializer

    def get_queryset(self):
        return Artist.objects.select_related(
            'city_of_birth',
            'city_of_living',
            'photo'
        ).prefetch_related(
            'favorited_by'
        )
