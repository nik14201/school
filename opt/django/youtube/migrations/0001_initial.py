# Generated by Django 3.0.5 on 2020-05-17 12:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelClassApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('youtube_src', models.URLField(blank=True, max_length=500, null=True, verbose_name='youtube url')),
                ('width', models.IntegerField(db_column='youtube_width', default=560, verbose_name='width')),
                ('height', models.IntegerField(db_column='youtube_height', default=315, verbose_name='width')),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 5, 17, 12, 21, 33, 598307))),
            ],
            options={
                'verbose_name': 'Видео с youtube',
                'verbose_name_plural': 'Видео',
            },
        ),
    ]
