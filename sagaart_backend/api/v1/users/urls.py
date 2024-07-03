from django.urls import path
from . import views

urlpatterns = [
    path('registration/',
         views.UserRegistrationViewSet.as_view({'post': 'create'}),
         name='user-register'),
    path('login/',
         views.UserLoginViewSet.as_view({'post': 'create'}),
         name='user-login'),
    path('update/<int:user_id>/',
         views.UserUpdateViewSet.as_view({'put': 'update'}),
         name='user-update'),
]
