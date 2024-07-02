from django.urls import include, path

urlpatterns = [
    path('', include('api.v1.artobjects.urls')),
    path('users/', include('api.v1.users.urls')),
]