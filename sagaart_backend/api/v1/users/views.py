from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from django.shortcuts import get_object_or_404
from .serializers import (
    UserLoginSerializer,
    UserRegistrationSerializer,
    UserUpdateSerializer
)

User = get_user_model()


class UserLoginViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(request, username=email, password=password)

            if user:
                access_token = AccessToken.for_user(user)
                return Response({
                    'message': 'Пользователь авторизован',
                    'access_token': str(access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Успешная регистрация',
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def update(self, request, user_id=None):
        if not request.user.is_authenticated:
            return Response({"message": "Пользователь не аутентифицирован"},
                            status=status.HTTP_401_UNAUTHORIZED)

        user = get_object_or_404(User, pk=user_id)

        if user != request.user:
            return Response({"message": "Нет доступа к изменению данных другого пользователя"},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = UserUpdateSerializer(instance=user,
                                          data=request.data,
                                          partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
