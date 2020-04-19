# Generated by Django 2.2.6 on 2020-02-05 17:40

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
                ('wind', models.TextField(blank=True, null=True, verbose_name='Ветер')),
                ('data', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блог',
            },
        ),
    ]