from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from . import models, serializers

class UserViewSet(viewsets.ModelViewSet):
  queryset = models.User.objects.all()
  serializer_class = serializers.UserSerializer
  permission_classes = [permissions.AllowAny]

class RecipeViewSet(viewsets.ModelViewSet):
  queryset = models.Recipe.objects.all()
  serializer_class = serializers.RecipeSerializer
  permission_classes = [permissions.IsAuthenticated]

class FavoriteViewSet(viewsets.ModelViewSet):
  queryset = models.Favorite.objects.all()
  serializer_class = serializers.FavoriteSerializer
  permission_classes = [permissions.IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(user = self.request.user)


class ProfileViewSet(viewsets.ModelViewSet):
  queryset = models.User.objects.all()
  permission_classes = [permissions.IsAuthenticated]
  def list(self, request):
    serializer = serializers.UserSerializer(request.user)
    return Response(serializer.data)