from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny

from artobjects.models import (Award, BaseArtObject, Category, Color, Genre,
                               MaterialArtObject, Style)
from core.models import City, SocialMedia
from .serializers_core import CitySerializer, SocialMediaSerializer
from .serializers_directories import (AwardSerializer, BaseArtObjectSerializer,
                                      CategorySerializer, ColorSerializer,
                                      GenreSerializer, MaterialArtObjectSerializer,
                                      StyleSerializer)


class AbstractDirectViewSet(viewsets.ReadOnlyModelViewSet):
    """Абстрактный класс для справочников."""
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)

    class Meta:
        abstract = True

class AwardViewSet(AbstractDirectViewSet):
    """Награды."""
    queryset = Award.objects.all()
    serializer_class = AwardSerializer


class BaseArtObjectViewSet(AbstractDirectViewSet):
    """Основы для произведения искусств."""
    queryset = BaseArtObject.objects.all()
    serializer_class = BaseArtObjectSerializer


class CategoryViewSet(AbstractDirectViewSet):
    """Категории."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ColorViewSet(AbstractDirectViewSet):
    """Награды."""
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class GenreViewSet(AbstractDirectViewSet):
    """Жанры."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MaterialArtObjectViewSet(AbstractDirectViewSet):
    """Чем написано произведение искусств."""
    queryset = MaterialArtObject.objects.all()
    serializer_class = MaterialArtObjectSerializer


class StyleViewSet(AbstractDirectViewSet):
    """Стили."""
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


class CityViewSet(AbstractDirectViewSet):
    """Города."""
    queryset = City.objects.all()
    serializer_class = CitySerializer


class SocialMediaViewSet(AbstractDirectViewSet):
    """Социальные сети."""
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
