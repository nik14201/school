from django.db import models
import datetime
import uuid
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Teacher(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    avatar = models.ImageField(
        upload_to='avatar/%Y/%m/%d',
        verbose_name = "Аватар",
        null=True,
        blank=True
        )
    email = models.EmailField(
        unique=True,
        verbose_name = "Email",
        max_length = 256,
        null=True,
        blank=True
        )
    first_name = models.CharField(
        verbose_name = "Имя",
        max_length = 256,
        null=True,
        blank=True
        )
    last_name = models.CharField(
        verbose_name = "Фамилия",
        max_length = 256,
        null=True,
        blank=True
        )
    patronymic = models.CharField(
        verbose_name = "Отчество",
        max_length = 256,
        null=True,
        blank=True
        )
    title = models.CharField(
        verbose_name = "Заголовок",
        max_length = 256,
        null=True,
        blank=True
        )
    phone = models.CharField(
        verbose_name = "Телефон",
        max_length = 256,
        null=True,
        blank=True
        )
 
    skype = models.CharField(
        verbose_name = "Skype",
        max_length = 256,
        null=True,
        blank=True
        )
    whatsapp = models.CharField(
        verbose_name = "Whatsapp",
        max_length = 256,
        null=True,
        blank=True
        )
    url_freelance = models.URLField(
        verbose_name = "Free-lance",
        max_length = 256,
        null=True,
        blank=True)
    url_facebook = models.URLField(
        verbose_name = "Facebook",
        max_length = 256,
        null=True,
        blank=True)
    url_vk = models.URLField(
        verbose_name = "VK",
        max_length = 256,
        null=True,
        blank=True)
    telegram = models.CharField(
        verbose_name = "Telegram",
        max_length = 256,
        null=True,
        blank=True
        )
    url_telegram = models.URLField(
        verbose_name = "Telegram URL",
        max_length = 256,
        null=True,
        blank=True)

    class Meta:
        default_related_name = 'user_teacher'
        default_permissions =('add', 'change', 'delete')
        verbose_name = "Профиль"
        verbose_name_plural = "Профиль"
        permissions = [('can_deliver_pizzas', 'Can deliver pizzas')]


# from django.contrib.auth.models import Permission
# from django.contrib.contenttypes.models import ContentType
#
# content_type = ContentType.objects.get_for_model(Teacher)
# permission = Permission.objects.create(
#     codename='can_publish',
#     name='Can Publish Posts',
#     content_type=content_type,
# )