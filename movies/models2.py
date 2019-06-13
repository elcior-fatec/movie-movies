from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class PremiosFilmes(models.Model):
    nome_premio = models.CharField(max_length=350)


class Filmes(models.Model):
    nome_filme = models.CharField(max_length=350)
    ano_lancamento = models.IntegerField(null=True, blank=True)
    avaliacao = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])


# Classe Associação
class FilmesPremiados(models.Model):
    id_premio = models.ForeignKey(PremiosFilmes, on_delete=models.CASCADE)
    id_filme = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    ano_premiacao = models.IntegerField()


class Paises(models.Model):
    nome_pais = models.CharField(max_length=30)


# Classe Associação
class PaisesOrigemFilme(models.Model):
    id_filme = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    id_pais = models.ForeignKey(Paises, on_delete=models.CASCADE)


class Artistas(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    id_pais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    sobrenome = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    nascimento = models.IntegerField(null=True, blank=True)
    falecimento = models.BooleanField()
    sexo = models.CharField(max_length=1, choices=SEXO)


class Atores(models.Model):
    id_artista = models.ForeignKey(Artistas, on_delete=models.CASCADE)


# Classe Associação
class AtuaramFilmes(models.Model):
    id_filme = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    id_ator = models.ForeignKey(Atores, on_delete=models.CASCADE)
    protagonista = models.BooleanField()
    antagonista = models.BooleanField()
    debute = models.BooleanField()


class PremiosAtuacao(models.Model):
    nome_premio = models.CharField(max_length=350)


# Classe Associação
class AtoresPremiados(models.Model):
    id_ator: models.ForeignKey(Atores, on_delete=models.CASCADE)
    id_filme: models.ForeignKey(Filmes, on_delete=models.CASCADE)
    id_premios_atores: models.ForeignKey(PremiosAtuacao, on_delete=models.CASCADE)
    ano_premiacao = models.IntegerField()


class Diretores(models.Model):
    id_artista = models.ForeignKey(Artistas, on_delete=models.CASCADE)


class PremiosDirecao(models.Model):
    nome_premio = models.CharField(max_length=350)


# Classe Associação
class DirigiramFilmes(models.Model):
    id_diretor = models.ForeignKey(Diretores, on_delete=models.CASCADE)
    id_filme = models.ForeignKey(Diretores, on_delete=models.CASCADE)


# Classe Associação
class PremiadosDirecao(models.Model):
    id_premio = models.ForeignKey(PremiosDirecao, on_delete=models.CASCADE)
    id_filme = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    id_diretor = models.ForeignKey(Diretores, on_delete=models.CASCADE)

