# Generated by Django 3.0.7 on 2020-06-18 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='like',
        ),
    ]