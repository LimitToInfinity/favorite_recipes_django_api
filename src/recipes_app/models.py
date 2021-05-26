from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
  name = models.CharField(max_length=50)
  users = models.ManyToManyField(User, related_name='users', through='Favorite')

  def __str__(self):
    return f'{self.id}: {self.name}'

class Favorite(models.Model):
  recipe = models.ForeignKey(Recipe, blank=True, null=True, related_name='favorites', on_delete=models.CASCADE)
  user = models.ForeignKey(User, blank=True, null=True, related_name='favorites', on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.id}: {self.user.username} likes {self.recipe.name}'