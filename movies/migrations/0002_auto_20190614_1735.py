# Generated by Django 2.2.2 on 2019-06-14 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filme',
            old_name='atores',
            new_name='ator',
        ),
        migrations.RenameField(
            model_name='filme',
            old_name='paises',
            new_name='pais',
        ),
        migrations.AddField(
            model_name='filme',
            name='diretor',
            field=models.ManyToManyField(through='movies.DirigiuFilme', to='movies.Diretor'),
        ),
    ]
