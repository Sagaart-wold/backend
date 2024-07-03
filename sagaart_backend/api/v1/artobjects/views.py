from rest_framework import mixins

from artobjects.models import Artist
from rest_framework.viewsets import GenericViewSet

from .serializers import ArtistReadListSerializer, ArtistReadRetrieveSerializer


class ArtistViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):

    def get_queryset(self):
        return Artist.objects.select_related(
            "city_of_birth", "city_of_living", "photo", 'city_of_birth__country', 'city_of_living__country'
        ).prefetch_related("favorited_by")

    def get_serializer_class(self):
        if self.action == 'list':
            return ArtistReadListSerializer
        return ArtistReadRetrieveSerializer
