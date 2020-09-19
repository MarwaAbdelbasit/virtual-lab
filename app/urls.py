from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('devices/', views.devices, name='devices'),
    path('register/', views.register, name='register'),
]
