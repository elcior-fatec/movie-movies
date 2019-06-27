from django.urls import path
from django.urls import include
from .views import (
    register_movies,
    list_movies,
    register_artist,
)

urlpatterns = [
    path('register/', register_movies, name='register_movies'),
    path('artist/', register_artist, name='register_artist'),
    path('list/', list_movies, name='list_movies'),
]
