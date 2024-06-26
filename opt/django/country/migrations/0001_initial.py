# Generated by Django 3.0.5 on 2020-05-17 12:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('_name', models.CharField(blank=True, max_length=512, null=True, verbose_name='Страна')),
                ('_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
                'db_table': 'country',
            },
        ),
    ]
