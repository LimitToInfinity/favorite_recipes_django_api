from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('users', views.UserViewSet)
router.register('recipes', views.RecipeViewSet)
router.register('favorites', views.FavoriteViewSet)
router.register('profile', views.ProfileViewSet)

urlpatterns = [
  path('', include(router.urls))
]
