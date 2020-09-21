from django.contrib import admin
from .models import Devices, Experiments, Accounts,Reservation,FAQ

# Register your models here.
admin.site.register(Devices)
admin.site.register(Experiments)
admin.site.register(Accounts)
admin.site.register(Reservation)
admin.site.register(FAQ)