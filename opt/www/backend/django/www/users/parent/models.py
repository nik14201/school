from django.db import models
import datetime
import uuid
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Parent(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="parent_set",
        related_query_name="parent",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('parent permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="parent_set",
        related_query_name="parent",
    )
    student = models.ForeignKey(
        'student.Student',
        related_name="student",
        on_delete=models.SET_NULL,
        verbose_name="parent_student",
        null=True,
        blank=True)
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

    def __str__(self):
        return self.email

    class Meta:
        default_related_name = 'user_parent'
        default_permissions = ('add', 'change', 'delete')
        verbose_name = "Профиль"
        verbose_name_plural = "Профиль"
        permissions = [('can_deliver_pizzas', 'Can deliver pizzas')]

# from django.contrib.auth.models import Permission
# from django.contrib.contenttypes.models import ContentType
#
# content_type = ContentType.objects.get_for_model(Parent)
# permission = Permission.objects.create(
#     codename='can_publish',
#     name='Can Publish Posts',
#     content_type=content_type,
# )