# Generated by Django 3.0.5 on 2020-04-19 16:16

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d', verbose_name='Аватар')),
                ('email', models.EmailField(blank=True, max_length=256, null=True, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=256, null=True, verbose_name='Отчество')),
                ('title', models.CharField(blank=True, max_length=256, null=True, verbose_name='Заголовок')),
                ('phone', models.CharField(blank=True, max_length=256, null=True, verbose_name='Телефон')),
                ('skype', models.CharField(blank=True, max_length=256, null=True, verbose_name='Skype')),
                ('whatsapp', models.CharField(blank=True, max_length=256, null=True, verbose_name='Whatsapp')),
                ('url_freelance', models.URLField(blank=True, max_length=256, null=True, verbose_name='Free-lance')),
                ('url_facebook', models.URLField(blank=True, max_length=256, null=True, verbose_name='Facebook')),
                ('url_vk', models.URLField(blank=True, max_length=256, null=True, verbose_name='VK')),
                ('telegram', models.CharField(blank=True, max_length=256, null=True, verbose_name='Telegram')),
                ('url_telegram', models.URLField(blank=True, max_length=256, null=True, verbose_name='Telegram URL')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='profile_set', related_query_name='profile', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='profile_set', related_query_name='profile', to='auth.Permission', verbose_name='student permissions')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профиль',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
