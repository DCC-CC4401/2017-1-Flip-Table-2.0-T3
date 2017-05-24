from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tag, Dish

# Register your models here.

admin.site.register(Tag)
admin.site.register(Dish)
