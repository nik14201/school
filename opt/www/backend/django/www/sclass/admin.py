from django.contrib import admin
from .models import ModelsModel as AdminModel, list_display

@admin.register(AdminModel)
class AdminModelAdmin(admin.ModelAdmin):
    list_display = list_display
