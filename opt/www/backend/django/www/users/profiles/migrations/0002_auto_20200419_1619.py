# Generated by Django 3.0.5 on 2020-04-19 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'default_permissions': ('add', 'change', 'delete'), 'default_related_name': 'user_profile', 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профиль'},
        ),
    ]