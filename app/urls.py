from django.urls import path
from . import views
from app.views import Register_view, Login_view

app_name = 'app'

urlpatterns = [
    path('devices/', views.devices, name='devices'),
    path('register/', Register_view.as_view(), name='register'),
    path('login/', Login_view.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
