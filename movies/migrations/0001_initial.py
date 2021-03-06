# Generated by Django 2.2.4 on 2019-09-01 16:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=256)),
                ('Description', models.TextField()),
                ('Rating', models.FloatField(null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('Run_Length', models.IntegerField(help_text='Enter run length in minutes')),
                ('popularity_index', models.IntegerField(blank=True, null=True, unique=True)),
                ('certificate', models.CharField(choices=[('U', 'U'), ('UA', 'U/A'), ('A', 'A'), ('R', 'R')], max_length=2)),
                ('Poster_Link', models.URLField(max_length=256, null='True')),
                ('Hor_Poster_Link', models.URLField(max_length=256, null='True')),
                ('Trailer_link', models.CharField(max_length=256, null='True')),
                ('ReleaseDate', models.DateField(null=True)),
                ('Genres', models.ManyToManyField(to='movies.Genre')),
                ('Languages', models.ManyToManyField(to='movies.Language')),
                ('stars', models.ManyToManyField(to='movies.Star')),
            ],
        ),
    ]
