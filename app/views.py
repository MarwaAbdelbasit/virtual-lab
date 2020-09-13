from django.shortcuts import render
from .models import Devices, Experiments

# Create your views here.
def devices(request):
    devices = Devices.objects.all()
    experiments = Experiments.objects.all()
    return render(request, 'app/devices.html', {'devices':devices,
    'experiments': experiments})
