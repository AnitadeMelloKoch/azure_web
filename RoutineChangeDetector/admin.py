from django.contrib import admin
from .models import UserData, UserRoutine

# Register your models here.
admin.site.register(UserData)
admin.site.register(UserRoutine)