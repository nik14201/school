from django.contrib import admin
from .models import *

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'temperature', 'wind']
