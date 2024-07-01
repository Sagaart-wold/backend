from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ArtistViewSet
from .views_directories import (AwardViewSet, BaseArtObjectViewSet,
                                CategoryViewSet, CityViewSet, ColorViewSet,
                                GenreViewSet, MaterialArtObjectViewSet,
                                SocialMediaViewSet, StyleViewSet)


router = DefaultRouter()
router.register("artists", ArtistViewSet, basename="artists")
# эндпоинты справочников
router.register('awards', AwardViewSet, basename='awards')
router.register('bases', BaseArtObjectViewSet, basename='bases')
router.register('categories', CategoryViewSet, basename='categories')
router.register('colors', ColorViewSet, basename='colors')
router.register('genres', GenreViewSet, basename='genres')
router.register('materials', MaterialArtObjectViewSet, basename='materials')
router.register('spheres', StyleViewSet, basename='spheres')
router.register('cities', CityViewSet, basename='cities')
router.register('socialmedias', SocialMediaViewSet, basename='socialmedias')


urlpatterns = [
    path("", include(router.urls)),
]
