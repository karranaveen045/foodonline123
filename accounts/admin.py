from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,UserProfile

class CustomUserAmin(UserAdmin):
    list_display = ("username","first_name","last_name","email","is_active","is_staff",'role')
    ordering=("-date_joined",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(User,CustomUserAmin)
admin.site.register(UserProfile)