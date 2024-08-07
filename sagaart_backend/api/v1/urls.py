from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


urlpatterns = [
    path('', include('api.v1.artobjects.urls')),
    path('users/', include('api.v1.users.urls')),
    path('articles/', include('api.v1.article.urls')),
]


schema_view = get_schema_view(
    openapi.Info(
        title="Șagaart API",
        default_version="v1",
        description="API Documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        'swagger/',
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        'redoc/',
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]