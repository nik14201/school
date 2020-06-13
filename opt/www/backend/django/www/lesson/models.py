from django.db import models
import datetime
import uuid
list_display = ['id', 'name', 'code']
verbose_name = "Урок"
verbose_name_plural = "Урок"
db_table = 'lesson'
app_label = 'lesson'


class MainModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    _subject = models.ForeignKey(
        'subject.MainModel',
        on_delete=models.SET_NULL,
        verbose_name="Предмет",
        null=True,
        blank=True
    )
    _sclass = models.ForeignKey(
        'sclass.MainModel',
        on_delete=models.SET_NULL,
        verbose_name="Класс",
        null=True,
        blank=True
    )
    _name = models.CharField(
        verbose_name="Name",
        max_length=512,
        null=True,
        blank=True
    )
    text = models.TextField(
        verbose_name = "Описание",
        null=True,
        blank=True
    )
    video_src = models.URLField(
        verbose_name = "video url",
        max_length = 500,
        null=True,
        blank=True
    )
    width = models.IntegerField(
        default=560,
        db_column = 'video_width',
        verbose_name="width"
    )
    height = models.IntegerField(
        default=315,
        db_column = 'video_height',
        verbose_name="width"
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
    def subject(self):
        return self._subject.name

    @subject.setter
    def subject(self, value):
        self._subject.name = value

    @property
    def sclass(self):
        return self._sclass.id

    @sclass.setter
    def sclass(self, value):
        self._sclass.id = value