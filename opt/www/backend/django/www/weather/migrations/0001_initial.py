# Generated by Django 3.0.5 on 2020-05-17 12:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=256, null=True, verbose_name='Город')),
                ('temperature', models.CharField(blank=True, max_length=10, null=True, verbose_name='Температура')),
                ('wind', models.CharField(blank=True, max_length=256, null=True, verbose_name='Ветер')),
                ('data', models.DateTimeField(default=datetime.datetime(2020, 5, 17, 12, 21, 32, 342488))),
            ],
            options={
                'verbose_name': 'Погода',
                'verbose_name_plural': 'Погода',
            },
        ),
    ]
