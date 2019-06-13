from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Paises(models.Model):
    nome_pais = models.CharField(max_length=30)


class Artistas(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    id_pais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    sobrenome = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    nascimento = models.IntegerField(null=True, blank=True)
    falecimento = models.BooleanField(default=False)
    sexo = models.CharField(max_length=1, choices=SEXO)


class PremiosAtuacao(models.Model):
    nome_premio = models.CharField(max_length=350)


class Atores(models.Model):
    artista = models.OneToOneField(Artistas, on_delete=models.CASCADE, primary_key=True)


class Diretores(models.Model):
    artista = models.OneToOneField(Artistas, on_delete=models.CASCADE, primary_key=True)


class PremiosFilmes(models.Model):
    nome_premio = models.CharField(max_length=350)


class PremiosDirecao(models.Model):
    nome_premio = models.CharField(max_length=350)


class Filmes(models.Model):
    nome_filme = models.CharField(max_length=350)
    ano_lancamento = models.IntegerField(null=True, blank=True)
    avaliacao = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    premio_filme = models.ManyToManyField(PremiosFilmes, through='FilmesPremiados')
    atores = models.ManyToManyField(Atores, through='AtuaramFilmes')
    paises = models.ManyToManyField(Paises)


# Classe Associação
class AtuaramFilmes(models.Model):
    id_filme = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    id_ator = models.ForeignKey(Atores, on_delete=models.CASCADE)
    protagonista = models.BooleanField(default=False)
    antagonista = models.BooleanField(default=False)
    debute = models.BooleanField(default=False)
    id_premio = models.ManyToManyField(PremiosAtuacao, through='PremioAtuacaoFilme')


# Classe Associação
class DirigiramFilmes(models.Model):
    id_filme = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    id_diretor = models.ForeignKey(Diretores, on_delete=models.CASCADE)
    id_premio = models.ManyToManyField(PremiosDirecao, through='PremioDirecaoFilme')


# Tabela de Associação
class PremioAtuacaoFilme(models):
    id_premio_atuacao = models.ForeignKey(PremiosAtuacao, on_delete=models.CASCADE)
    id_filme = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    id_ator = models.ForeignKey(Atores, on_delete=models.CASCADE)
    ano_premio = models.IntegerField()


# Tabela de Associação
class PremioDirecaoFilme(models):
    id_premio_direcao = models.ForeignKey(PremiosAtuacao, on_delete=models.CASCADE)
    id_filme = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    id_diretor = models.ForeignKey(Diretores, on_delete=models.CASCADE)
    ano_premio = models.IntegerField()


# Tabela de Associação
class FilmesPremiados(models.Model):
    id_premio = models.ForeignKey(PremiosFilmes, on_delete=models.CASCADE)
    id_filme = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    ano_premiacao = models.IntegerField()


