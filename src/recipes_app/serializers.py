from pdb import Pdb
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from . import models

class UserObjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email')

class RecipeObjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Recipe
    fields = '__all__'

class FavoriteObjectSerializer(serializers.ModelSerializer):
  recipe = RecipeObjectSerializer(many=False)

  class Meta:
    model = models.Favorite
    fields = ('id', 'recipe', 'user')

class UserSerializer(serializers.ModelSerializer):
  favorites = FavoriteObjectSerializer(many=True, required=False)
  class Meta:
    model = User
    fields = ('id', 'username', 'password', 'email', 'favorites')

  def create(self, validated_data):
    user = User.objects.create(
      username = validated_data['username'],
      password = make_password(validated_data['password']),
      email = validated_data['email'],
    )
    user.save()
    token = Token.objects.create(user=user)
    return user


class RecipeSerializer(serializers.ModelSerializer):
  users = UserObjectSerializer(many=True)
  favorites = FavoriteObjectSerializer(many=True)
  
  class Meta:
    model = models.Recipe
    fields = ('id', 'name', 'users', 'favorites')

class FavoriteSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Favorite
    fields = ('id', 'recipe', 'user')

