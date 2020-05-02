from django.contrib import admin
from .models import *

@admin.register(ModelClassApp)
class ModelClassAppAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date']
