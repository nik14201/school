from django.db import models
import datetime
import uuid
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

class Student(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="student_set",
        related_query_name="student",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('student permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="student_set",
        related_query_name="student",
    )
    _sclass = models.ForeignKey(
        'sclass.MainModel',
        on_delete=models.SET_NULL,
        verbose_name="Класс",
        null=True,
        blank=True
    )
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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        default_related_name = 'user_student'
        default_permissions = ('add', 'change', 'delete')
        verbose_name = "Ученик"
        verbose_name_plural = "Ученик"


    @property
    def sclass(self):
        return self._sclass

    @sclass.setter
    def sclass(self, value):
        self._sclass = value