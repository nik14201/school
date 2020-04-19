from django.db import models
import datetime

list_display = ['id', 'name_ru', 'name_en']
verbose_name = "Страна"
verbose_name_plural = "Страны"
db_table = 'country'
app_label = 'country'

class ModelsModel(models.Model):
    _name = models.CharField(
        verbose_name = "Страна",
        max_length = 512,
        null=True,
        blank=True
        )
    _code = models.CharField(
        verbose_name = "code",
        max_length = 20,
        null=True,
        blank=True
        )

    class Meta:
        verbose_name = verbose_name
        verbose_name_plural = verbose_name_plural
        db_table = db_table
        app_label = app_label

    def __str__(self):
        return "%s  %s" % (self._name,  self._code)

    @property
    def name(self):
        return  self._name
    @name.setter
    def name(self,value):
        self._name = value

    @property
    def code(self):
        return  self._code

    @code.setter
    def code(self,value):
        self._code = value
