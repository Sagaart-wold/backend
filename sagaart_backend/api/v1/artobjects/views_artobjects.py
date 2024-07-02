from rest_framework import mixins, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from artobjects.models import ArtObject
from rest_framework.viewsets import GenericViewSet

from .serializers import (ArtObjectListSerializer,
                          ArtObjectRetrieveSerializer)


class ArtObjectViewSet(mixins.RetrieveModelMixin,
                       mixins.ListModelMixin, GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('^name',)
    filterset_fields = ('category', 'genre', 'style', 'orientation',
                        'tag_size', 'colors', 'artist')

    def get_queryset(self):
        return ArtObject.objects.all().select_related(
            'artist', 'category', 'genre', 'material_art_object',
            'base_art_object', 'style', 'collection', 'main_image',
            'city_sold__country', 'owner',
        ).prefetch_related('images', 'colors', 'favourited_by')

    def get_serializer_class(self):
        if self.action == 'list':
            return ArtObjectListSerializer
        return ArtObjectRetrieveSerializer
