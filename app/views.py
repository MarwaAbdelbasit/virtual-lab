from django.shortcuts import render, redirect
from .models import Devices, Experiments, Accounts
from . import forms

# Create your views here.
def devices(request):
    devices = Devices.objects.all()
    experiments = Experiments.objects.all()
    return render(request, 'app/devices.html', {'devices':devices,
    'experiments': experiments})

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
