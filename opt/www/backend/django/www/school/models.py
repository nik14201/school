from django.db import models
import datetime
import uuid
list_display = ['id', 'name', 'code']
verbose_name = "Школа"
verbose_name_plural = "Школа"
db_table = 'school'
app_label = 'school'


class MainModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    _city = models.ForeignKey(
        'city.MainModel',
        on_delete=models.SET_NULL,
        verbose_name="Город",

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
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
