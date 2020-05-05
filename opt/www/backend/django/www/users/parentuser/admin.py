from django.utils.html import format_html
from django.contrib import admin
from .models import ParentUser, ParentStudentMM


@admin.register(ParentUser)
class UserTravellAdmin(admin.ModelAdmin):
    list_display = ['img_avatar', 'email']
    search_fields = ['email']

    def img_avatar(self, obj):
        return format_html("<img width='100' height='100' src='%s'/>" % ("/media/" + str(obj.avatar)))

    img_avatar.allow_tags = True
    img_avatar.short_description = "Фото"


@admin.register(ParentStudentMM)
class ParentStudentMMAdmin(admin.ModelAdmin):
    list_display = ['parent', 'student']




from .models import TokenParent
@admin.register(TokenParent)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created', )
    fields = ('user',)
    ordering = ('-created',)

