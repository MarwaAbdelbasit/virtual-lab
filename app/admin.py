from django.contrib import admin
from .models import Devices
from .models import Experiments,Reservation,faq

# Register your models here.
admin.site.register(Devices)
admin.site.register(Experiments)
admin.site.register(Reservation)
admin.site.register(faq)

