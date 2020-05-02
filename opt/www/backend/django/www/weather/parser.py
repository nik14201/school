# -*- coding: utf-8 -*-
import scrapy
from weather.models import Weather

class YandexSpider(scrapy.Spider):
    name = 'yandex'
    allowed_domains = ['yandex.ru']
    start_urls = ['https://yandex.ru/pogoda/stavropol']

    def parse(self, response):
        print("!!!!PARSE!!!!", response.css('div.term__value').xpath('@aria-label').get())
        try:
            Weather.objects.create(
            	city='Ставрополь', 
            	temperature=response.css('div.fact__temp span.temp__value::text').get(),
            	wind=response.css('div.term__value').xpath('@aria-label').get()
            	)
        except Exception as e:
            print(e)
        return 0



