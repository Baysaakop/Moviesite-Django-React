# Generated by Django 2.2.7 on 2019-11-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20191114_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
