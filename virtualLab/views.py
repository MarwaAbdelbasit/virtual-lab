from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.models import *

def home(request):
    obj = User.objects.all()
    return render(request, 'base_layout.html', {'obj': obj})
