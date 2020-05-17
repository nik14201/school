from django.db import models
import datetime
import uuid
list_display = ['id', 'name', 'code']
verbose_name = "Дневник"
verbose_name_plural = "Дневник"
db_table = 'diary'
app_label = 'diary'


class MainModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    _teacher = models.ForeignKey(
        'teacher.User',
        related_name='diary_teacher',
        on_delete=models.SET_NULL,
        verbose_name="Учитель",
        null=True,
        blank=True
    )
    _student = models.ForeignKey(
        'student.User',
        related_name='diary_student',
        on_delete=models.SET_NULL,
        verbose_name="Ученик",
        null=True,
        blank=True
    )
    _homework = models.ForeignKey(
        'homework.MainModel',
        related_name='diary_homework',
        on_delete=models.SET_NULL,
        verbose_name="Домашнее задание",
        null=True,
        blank=True
    )
    _name = models.CharField(
        verbose_name="Name",
        max_length=512,
        null=True,
        blank=True
    )
    _code = models.CharField(
        verbose_name="Code",
        max_length=256,
        null=True,
        blank=True
    )

    def __str__(self):
        return "%s  %s" % (self._name, self._code)

    class Meta:
        verbose_name = verbose_name
        verbose_name_plural = verbose_name_plural
        db_table = db_table
        app_label = app_label

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def student(self):
        return self._student

    @student.setter
    def student(self, value):
        self._student = value


    @property
    def homework(self):
        return self._homework

    @homework.setter
    def homework(self, value):
        self._homework = value