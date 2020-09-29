from django.http import HttpResponse
from django.shortcuts import render, redirect

def base_layout_view(request):
    return render(request, 'base_layout.html')

# home page view
def home_view(request):
    return render(request, 'home.html')
