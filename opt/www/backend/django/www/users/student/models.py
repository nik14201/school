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


from rest_framework.authtoken.models import Token
class Token(Token):
    user = models.OneToOneField(
        'student.User', related_name='auth_token',
        on_delete=models.CASCADE, verbose_name=_("Student")
    )
    class Meta:
        abstract = False
        db_table = 'token_student'
        app_label = 'student'