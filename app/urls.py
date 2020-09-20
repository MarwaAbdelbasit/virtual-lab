from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('devices/', views.devices, name='devices'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('Add_Question', views.A_Q, name='Add_Question'),
    path('Add_Device', views.Add_device, name='Add_Device'),
]
