# Generated by Django 2.2.7 on 2019-11-13 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='imdb_rating',
            new_name='rating',
        ),
    ]