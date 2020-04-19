from django.utils.html import format_html
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile

#admin.site.register(User, UserAdmin)

@admin.register(Profile)
class UserTravellAdmin(admin.ModelAdmin):
    list_display = ['img_avatar', 'email']
    search_fields=['email']

    def img_avatar(self, obj):
        return format_html("<img width='100' height='100' src='%s'/>" % ("/media/"+str(obj.avatar)))
    img_avatar.allow_tags = True
    img_avatar.short_description = "Фото"