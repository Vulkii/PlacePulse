# Generated by Django 3.2.3 on 2024-01-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='latitude',
            field=models.FloatField(default=57.54, verbose_name='Широта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='longitude',
            field=models.FloatField(default=36.34, verbose_name='Долгота'),
            preserve_default=False,
        ),
    ]
