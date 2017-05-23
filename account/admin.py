from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client, Peddler, Established, Dish

# Register your models here.

admin.site.register(Client)
admin.site.register(Peddler)
admin.site.register(Established)
admin.site.register(Dish)
