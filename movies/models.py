from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Pais(models.Model):
    nome_pais = models.CharField(max_length=30, verbose_name='Nome do País', unique=True)

    def __str__(self):
        return '{}'.format(self.nome_pais)

    class Meta:
        verbose_name_plural = "Paises"
        ordering = ('nome_pais',)


class Artista(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    sobrenome = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    nascimento = models.IntegerField(null=True, blank=True, verbose_name='Ano de Nascimento')
    falecimento = models.BooleanField(default=False)
    sexo = models.CharField(max_length=1, choices=SEXO)

    def __str__(self):
        return '{}, {}'.format(self.sobrenome, self.nome)

    class Meta:
        ordering = ('sobrenome',)


class PremioAtuacao(models.Model):
    nome_premio = models.CharField(max_length=350, verbose_name='Nome do Prêmio')

    def __str__(self):
        return '{}'.format(self.nome_premio)

    class Meta:
        verbose_name_plural = "Prêmios cedidos para atuações"
        ordering = ('nome_premio',)


class Ator(models.Model):
    artista = models.OneToOneField(Artista, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return '{}'.format(self.artista)

    class Meta:
        verbose_name_plural = "Atores"
        ordering = ('artista',)


class Diretor(models.Model):
    artista = models.OneToOneField(Artista, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return '{}'.format(self.artista)

    class Meta:
        verbose_name_plural = "Diretores"
        ordering = ('artista',)


class PremioFilme(models.Model):
    nome_premio = models.CharField(max_length=350, verbose_name='Nome do Prêmio')

    def __str__(self):
        return '{}'.format(self.nome_premio)

    class Meta:
        verbose_name_plural = "Prêmios cedidos aos filmes"
        ordering = ('nome_premio',)


class PremioDirecao(models.Model):
    nome_premio = models.CharField(max_length=350, verbose_name='Nome do Prêmio')

    def __str__(self):
        return '{}'.format(self.nome_premio)

    class Meta:
        verbose_name_plural = "Prêmios ceditos pela direção"
        ordering = ('nome_premio',)


class Genero(models.Model):
    genero = models.CharField(max_length=50, verbose_name='Gênero')

    def __str__(self):
        return '{}'.format(self.genero)

    class Meta:
        verbose_name_plural = "Gêneros"
        ordering = ('genero',)


class Filme(models.Model):
    nome_filme = models.CharField(max_length=350, verbose_name='Nome do Filme')
    nome_original = models.CharField(max_length=350, verbose_name='Nome Original do Filme', blank=True, null=True)
    ano_lancamento = models.IntegerField(verbose_name='Lançamento')
    avaliacao = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        verbose_name='Avaliação'
    )
    genero = models.ManyToManyField(Genero)
    metragem = models.PositiveIntegerField(verbose_name='Duração (min)')
    classificacao = models.CharField(max_length=10, verbose_name='Classificação etária')
    premio_filme = models.ManyToManyField(PremioFilme, through='FilmePremiado')
    ator = models.ManyToManyField(Ator, through='AtuouFilme')
    diretor = models.ManyToManyField(Diretor, through='DirigiuFilme')
    pais = models.ManyToManyField(Pais)

    def __str__(self):
        return '{}'.format(self.nome_filme)

    class Meta:
        ordering = ('nome_filme', 'ano_lancamento',)


# Classe Associação
class AtuouFilme(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    ator = models.ForeignKey(Ator, on_delete=models.CASCADE)
    protagonista = models.BooleanField(default=False)
    antagonista = models.BooleanField(default=False)
    debute = models.BooleanField(default=False)
    premio = models.ManyToManyField(PremioAtuacao, through='PremioAtuacaoFilme')

    def __str__(self):
        return '{} - {}'.format(self.filme, self.ator)

    class Meta:
        verbose_name_plural = "Atuaram no filmes"
        ordering = ('filme', 'ator',)


# Classe Associação
class DirigiuFilme(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)
    premio = models.ManyToManyField(PremioDirecao, through='PremioDirecaoFilme')

    def __str__(self):
        return '{} - {}'.format(self.filme, self.diretor)

    class Meta:
        verbose_name_plural = "Dirigiram os filmes"
        ordering = ('filme', 'diretor',)


# Tabela de Associação
class PremioAtuacaoFilme(models.Model):
    premio_atuacao = models.ForeignKey(PremioAtuacao, on_delete=models.CASCADE)
    atuacao = models.ForeignKey(AtuouFilme, on_delete=models.CASCADE)
    ano_premio = models.IntegerField(verbose_name='Ano da premiação')

    def __str__(self):
        return '{} - {} {}'.format(self.atuacao, self.premio_atuacao, self.ano_premio)

    class Meta:
        verbose_name_plural = "Prêmios pelas atuações"
        ordering = ('ano_premio', 'premio_atuacao', 'atuacao')


# Tabela de Associação
class PremioDirecaoFilme(models.Model):
    premio_direcao = models.ForeignKey(PremioDirecao, on_delete=models.CASCADE)
    direcao = models.ForeignKey(DirigiuFilme, on_delete=models.CASCADE)
    ano_premio = models.IntegerField(verbose_name='Premiação')

    def __str__(self):
        return '{} - {} {}'.format(self.direcao, self.premio_direcao, self.ano_premio)

    class Meta:
        verbose_name_plural = "Prêmios pelas direções"
        ordering = ('ano_premio', 'premio_direcao', 'direcao',)


# Tabela de Associação
class FilmePremiado(models.Model):
    premio = models.ForeignKey(PremioFilme, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    ano_premiacao = models.IntegerField(verbose_name='Premiação')

    def __str__(self):
        return '{} - {} {}'.format(self.filme, self.premio, self.ano_premiacao)

    class Meta:
        verbose_name_plural = "Filmes premiados"
        ordering = ('ano_premiacao', 'premio', 'filme',)
