from django.shortcuts import render
from .models import Devices, Experiments,faq
from . import forms

# Create your views here.
def devices(request):
    devices = Devices.objects.all()
    experiments = Experiments.objects.all()
    return render(request, 'app/devices.html', {'devices':devices,
    'experiments': experiments})
def A_Q(request):
     if request.method == 'POST':
        form = forms.AddQuestion(request.POST)
        if form.is_valid():
            # save account to database
            form.save()
            return redirect('home')
     else:
        form = forms.AddQuestion()
     return render(request, 'app/A_Q.html', {'form': form})
def Add_device(request):
     if request.method == 'POST':
        form = forms.AddDevice(request.POST)
        if form.is_valid():
            # save account to database
            form.save()
            return redirect('home')
     else:
        form = forms.AddDevice()
     return render(request, 'app/Add-device.html', {'form': form})