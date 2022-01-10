from django.db import models
from django.contrib.auth.models import Permission, Group
from django.utils.translation import gettext_lazy as _
from abstract.models import AbstractUser

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="teacher_set",
        related_query_name="teacher",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('student permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="teacher_set",
        related_query_name="teacher",
    )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        default_related_name = 'user_teacher'
        default_permissions =('add', 'change', 'delete')
        verbose_name = "Учитель"
        verbose_name_plural = "Учитель"


from rest_framework.authtoken.models import Token
class Token(Token):
    user = models.OneToOneField(
        'teacher.User', related_name='auth_token',
        on_delete=models.CASCADE, verbose_name=_("Teacher")
    )
    class Meta:
        abstract = False
        db_table = 'token_teacher'
        app_label = 'teacher'