from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('devices/', views.devices, name='devices'),
    path('FAQ/', views.faq, name='faq'),
    path('register/', views.register, name='register'),
    path('Add/', views.AddQuestion, name='AddQuestion'),
    path('AddDevice/', views.AddDevice, name='AddDevice'),
]
