# Generated by Django 3.0.5 on 2020-05-03 17:08

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0002_auto_20200503_1708'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d', verbose_name='Аватар')),
                ('email', models.EmailField(max_length=256, unique=True, verbose_name='Email')),
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
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='parent_set', related_query_name='parent', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'Родитель',
                'verbose_name_plural': 'Родитель',
                'default_permissions': ('add', 'change', 'delete'),
                'default_related_name': 'user_parent',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TokenParent',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token_parent', to=settings.AUTH_USER_MODEL, verbose_name='Parent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParentStudentMM',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_mm_student', to=settings.AUTH_USER_MODEL, verbose_name='parent_mm_student')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_mm_parent', to='student.Student', verbose_name='student_mm_parent')),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='student',
            field=models.ManyToManyField(blank=True, null=True, related_name='student', through='parent.ParentStudentMM', to='student.Student', verbose_name='parent_student'),
        ),
        migrations.AddField(
            model_name='parent',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='parent_set', related_query_name='parent', to='auth.Permission', verbose_name='parent permissions'),
        ),
    ]
