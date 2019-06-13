from django.http import HttpResponse
from django.shortcuts import render


def register_movies(request):
    return HttpResponse('Ola filmes!')
