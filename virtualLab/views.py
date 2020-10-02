from django.http import HttpResponse
from django.shortcuts import render, redirect
from app import forms
from app.models import Coupon
from django.contrib import messages

# def base_layout_view(request):
#     return render(request, 'base_layout.html')

# home page view
def home_view(request):
    return render(request, 'home.html')
