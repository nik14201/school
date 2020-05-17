from django.db import models
from django.contrib.auth.models import Permission, Group
from django.utils.translation import gettext_lazy as _
from abstract.models import AbstractUser
import uuid

class User(AbstractUser):
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
    student = models.ManyToManyField(
        'student.User',
        related_name="student",
        verbose_name="parent_student",
        through='ParentStudentMM',
        null=True,
        blank=True
    )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        default_related_name = 'user_parent'
        default_permissions = ('add', 'change', 'delete')
        verbose_name = "Родитель"
        verbose_name_plural = "Родитель"


class ParentStudentMM(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey('parent.User',
                               related_name="parent_mm_student",
                               on_delete=models.SET_NULL,
                               verbose_name="parent_mm_student",
                               null=True,
                               blank=True)
    student = models.ForeignKey('student.User',
                                related_name="student_mm_parent",
                                on_delete=models.SET_NULL,
                                verbose_name="student_mm_parent",
                                null=True,
                                blank=True)


from rest_framework.authtoken.models import Token

class Token(Token):
    user = models.OneToOneField(
        'parent.User', related_name='auth_token',
        on_delete=models.CASCADE, verbose_name=_("Parent")
    )
    class Meta:
        abstract = False
        db_table = 'token_parent'
        app_label = 'parent'
