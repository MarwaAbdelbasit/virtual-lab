from django.shortcuts import render, redirect
from .models import Devices, Experiments, Accounts,FAQ
from . import forms

# Create your views here.
def devices(request):
    devices = Devices.objects.all()
    experiments = Experiments.objects.all()
    return render(request, 'app/devices.html', {'devices':devices,
    'experiments': experiments})
def faq(request):
    faq = FAQ.objects.all()
    return render(request, 'app/faq.html', {'faq':faq})    

def register(request):
    if request.method == 'POST':
        form = forms.AccountsForm(request.POST)
        if form.is_valid():
            # save account to database
            form.save()
            return redirect('home')
    else:
        form = forms.AccountsForm()
    return render(request, 'app/register.html', {'form': form})

def AddQuestion(request):
    if request.method == 'POST':
        form = forms.AddQForm(request.POST)
        if form.is_valid():
            # save account to database
            form.save()
            return redirect('home')
    else:
        form = forms.AddQForm()
    return render(request, 'app/AddDevice.html', {'form': form})
def AddDevice(request):
    if request.method == 'POST':
        form = forms.AddDeviceForm(request.POST)
        if form.is_valid():
            # save account to database
            form.save()
            return redirect('home')
    else:
        form = forms.AddDeviceForm()
    return render(request, 'app/AddDevice.html', {'form': form})          