# Generated by Django 5.0.4 on 2024-05-05 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moovies', '0002_movie_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_url',
            field=models.URLField(blank=True),
        ),
    ]