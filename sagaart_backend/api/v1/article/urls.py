from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article-list'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='article-detail'),
]
