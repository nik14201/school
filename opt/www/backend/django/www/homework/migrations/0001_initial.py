# Generated by Django 3.0.5 on 2020-05-17 12:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lesson', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('_name', models.CharField(blank=True, max_length=512, null=True, verbose_name='Name')),
                ('_code', models.CharField(blank=True, max_length=256, null=True, verbose_name='Code')),
                ('_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lesson.MainModel', verbose_name='Урок')),
            ],
            options={
                'verbose_name': 'Домашнее задание',
                'verbose_name_plural': 'Домашнее задание',
                'db_table': 'homework',
            },
        ),
    ]
