from django.contrib import admin
from .models import Client, Peddler, Established

# Register your models here.

admin.site.register(Client)
admin.site.register(Peddler)
admin.site.register(Established)
