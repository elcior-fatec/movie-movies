"""
Documantação para relacionamento ManyToMany: https://docs.djangoproject.com/pt-br/2.2/topics/db/models/
Texto auxiliar para relacionamento ManyToMany: https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/
Usar ManyToMany em Templates:
    https://stackoverflow.com/questions/4270330/django-show-a-manytomanyfield-in-a-template#4270839
"""
from django.http import HttpResponse
from django.shortcuts import render
from movies.models import Filme, Diretor, Ator, Genero, Pais


def register_movies(request):
    return HttpResponse('Registro dos filmesgi')


def list_movies(request, template_name='filmes/lista-filmes.html'):
    filmes = Filme.objects.all()
    return render(request, template_name, {'filmes': filmes})
