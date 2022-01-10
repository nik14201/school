from __future__ import absolute_import, unicode_literals
import requests
import django
django.setup()
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
import time
from threading import Thread
import random
from .parser import YandexSpider

THREAD_LIST={}

class ServiceThread(Thread):
    """
    A threading example
    """
    def __init__(self, name, ServiceClassThread):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name
        self.ClassThread = ServiceClassThread

    def run(self):
        """Запуск потока"""
        i =random.randint(1, 3)
        msg = "%s is running" % self.name
        print(msg)
        #time.sleep(i)
        print("thread end: "+str(i))
        try:
            runner = CrawlerRunner()
            runner.crawl(self.ClassThread)
            d = runner.join()
            d.addBoth(lambda _: reactor.stop())
            reactor.run()
            print(msg)
        except Exception as e:
            print("Error 1:",msg,'   ', e)
            exit()



def StartScrapy():
    print(THREAD_LIST)
    name = "ScrapyYandex"
    # if THREAD_LIST:
    #     if THREAD_LIST[name].isAlive():
    #         return
    #     else:
    #         THREAD_LIST[name].join()
    #         del THREAD_LIST[name]
    print("===============Start Tasks ==============")
    name = "ScrapyYandex"
    print("Start new: ", name)
    my_thread = ServiceThread(name, YandexSpider)
    my_thread.setName(name)
    my_thread.start()
    my_thread.join()
    #THREAD_LIST.update({my_thread.name: my_thread})


