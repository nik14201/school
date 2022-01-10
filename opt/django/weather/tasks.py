from __future__ import absolute_import, unicode_literals
from celery import Celery, task
import  datetime
from .services import StartScrapy


@task.periodic_task(run_every=datetime.timedelta(seconds=10))
def GetWeatherTask():
    print("GetWeatherTask")
    StartScrapy()



