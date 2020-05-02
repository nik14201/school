from django.db import models
import datetime
# Create your models here.


class ModelClassApp(models.Model):
    title = models.CharField(
        verbose_name = "Заголовок",
        max_length = 256,
        null=True,
        blank=True
        )
    text = models.TextField(
        verbose_name = "Описание",
        null=True,
        blank=True
    )
    youtube_src = models.URLField(
        verbose_name = "youtube url",
        max_length = 500,
        null=True,
        blank=True
    )
    width = models.IntegerField(
        default=560,
        db_column = 'youtube_width',
        verbose_name="width"
    )
    height = models.IntegerField(
        default=315,
        db_column = 'youtube_height',
        verbose_name="width"
    )
    date= models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.datetime.now())

    class Meta:
        verbose_name = "Видео с youtube"
        verbose_name_plural = "Видео"
        

