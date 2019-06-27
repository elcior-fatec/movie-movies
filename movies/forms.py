from django.forms import ModelForm
from .models import Filme, Artista


class MoviesInsertForm(ModelForm):
    class Meta:
        model = Filme
        fields = [
            'nome_filme',
            'nome_original',
            'ano_lancamento',
            'avaliacao',
            'genero',
            'metragem',
            'classificacao',
            'premio_filme',
            'ator',
            'diretor',
            'pais',
        ]


class ArtistsInsertForm(ModelForm):
    class Meta:
        model = Artista
        fields = [
            'sobrenome',
            'nome',
            'pais',
            'nascimento',
            'falecimento',
            'sexo'
        ]
