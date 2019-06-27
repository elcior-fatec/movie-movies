"""
Documantação para relacionamento ManyToMany: https://docs.djangoproject.com/pt-br/2.2/topics/db/models/
Texto auxiliar para relacionamento ManyToMany: https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/
Usar ManyToMany em Templates:
    https://stackoverflow.com/questions/4270330/django-show-a-manytomanyfield-in-a-template#4270839
"""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from movies.models import (
    Filme,
    Diretor,
    Ator,
    Genero,
    Pais
)
from .forms import (
    MoviesInsertForm,
    ArtistsInsertForm
)


def register_movies(request):
    form = MoviesInsertForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('register_movies')
    return render(request, 'movies-form.html', {'form': form})


def register_artist(request):
    form = ArtistsInsertForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('register_artist')
    return render(request, 'artist-form.html', {'form': form})


def list_movies(request, template_name='lista-filmes.html'):
    filmes = Filme.objects.all()
    return render(request, template_name, {'filmes': filmes})
