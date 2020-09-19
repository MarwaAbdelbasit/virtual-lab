from django.contrib import admin
from .models import Devices, Experiments, Accounts

# Register your models here.
admin.site.register(Devices)
admin.site.register(Experiments)
admin.site.register(Accounts)
