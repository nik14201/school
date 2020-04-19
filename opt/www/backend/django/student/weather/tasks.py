from __future__ import absolute_import, unicode_literals
import django
django.setup()
import json
import requests
import os
from celery import Celery, task
import  datetime
from .models import *
from etc.celery import app
from .service import ServiceWeather


@task.periodic_task(run_every=datetime.timedelta(seconds=120))
def GetWeatherTask():
    print("GetWeatherTask")
    service = ServiceWeather()
    service.url = 'https://yandex.ru'
    service.GetWeather()
    del service


