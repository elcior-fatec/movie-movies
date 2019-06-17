from django.urls import path
from django.urls import include
from .views import (
    register_movies,
    list_movies,
)

urlpatterns = [
    path('register/', register_movies, name='register_movies'),
    path('list/', list_movies, name='list_movies'),
]
