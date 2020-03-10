from django.db import models
import datetime
# Create your models here.


class Weather(models.Model):
    city = models.CharField(
        verbose_name = "Город",
        max_length = 256,
        null=True,
        blank=True
        )
    temperature = models.CharField(
        verbose_name = "Температура",
        max_length = 10,
        null=True,
        blank=True
        )
    wind = models.CharField(
        verbose_name = "Ветер",
        max_length = 256,
        null=True,
        blank=True
        )
    data= models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.datetime.now())

    class Meta:
        verbose_name = "Погода"
        verbose_name_plural = "Погода"