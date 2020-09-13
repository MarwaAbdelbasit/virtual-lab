from django.contrib import admin
from .models import Devices
from .models import Experiments

# Register your models here.
admin.site.register(Devices)
admin.site.register(Experiments)
