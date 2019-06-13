from django.urls import path
from django.urls import include
from .views import register_movies


urlpatterns = [
    path('movies/', register_movies, name='register_movies'),
]
