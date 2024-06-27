from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ArtistViewSet

router = DefaultRouter()
router.register('artists', ArtistViewSet, basename='artists')

urlpatterns = [
    path('', include(router.urls)),
]
