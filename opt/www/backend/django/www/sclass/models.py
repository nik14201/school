from django.db import models
import datetime
import uuid

list_display = ['id', 'school', 'letter','datecreate']
verbose_name = "Класс"
verbose_name_plural = "Класс"
db_table = 'sclass'
app_label = 'sclass'


class MainModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    _school = models.ForeignKey(
        'school.MainModel',
        on_delete=models.SET_NULL,
        verbose_name="Школа",
        related_name='sclass_school',
        null=True,
        blank=True
    )
    _letter = models.ForeignKey(
        'sclass.ClassLetter',
        on_delete=models.SET_NULL,
        verbose_name="Буква класса",
        related_name='sclass_letter',
        null=True,
        blank=True
    )
    _datecreate = models.DateField(
        verbose_name="Год создания 1-го класса",
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
        default=datetime.datetime.now()
    )
    _active = models.BooleanField(default=True)

    def __str__(self):
        return "%s  %s" % (self._name, self._code)

    class Meta:
        verbose_name = verbose_name
        verbose_name_plural = verbose_name_plural
        db_table = db_table
        app_label = app_label

    @property
    def letter(self):
        return self._letter

    @letter.setter
    def letter(self, value):
        self._letter = value

    @property
    def datecreate(self):
        return self._datecreate

    @datecreate.setter
    def datecreate(self, value):
        self._datecreate = value

    @property
    def school(self):
        return self._school

    @school.setter
    def school(self, value):
        self._school = value

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value


class ClassLetter(models.Model):
    _name = models.CharField(
        verbose_name="Name",
        max_length=4,
        null=True,
        blank=True
    )

    def __str__(self):
        return "%s " % (self._name)

    class Meta:
        verbose_name = 'Буква класса'
        verbose_name_plural = "Буквы класса"
        db_table = 'class_letter'
        app_label = 'sclass'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value