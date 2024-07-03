from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters, permissions, mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from artobjects.models import ArtObject
from shoppingcart.models import ShoppingCart
from .serializers import (ArtObjectListSerializer,
                          ArtObjectRetrieveSerializer,
                          ShoppingCartSerializer)


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

    @action(
        methods=['post', 'delete'],
        detail=True,
        permission_classes=[permissions.IsAuthenticated]
    )
    def shopping_cart(self, request, pk=None):
        """"Обработчик для добавления и удаления объекта в корзину
        залогиненного пользователя."""
        artobject = self.get_object()
        user = self.request.user
        print(artobject)
        print(user)
        serializer = ShoppingCartSerializer(
            data={'user': user, 'artobject': artobject},
            context={'request': request}
        )
        print(serializer.is_valid())
        if request.method == 'POST':
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        obj_cart = ShoppingCart.objects.filter(
            user=user,
            artobject=artobject
        )
        if obj_cart.exists():
            obj_cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {'errors': 'This recipe is not in shopping cart!'},
            status=status.HTTP_400_BAD_REQUEST
        )
