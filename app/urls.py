from django.urls import path
from . import views
from app.views import Register_view, Login_view

app_name = 'app'

urlpatterns = [
    path('devices/', views.devices, name='devices'),
    path('register/', Register_view.as_view(), name='register'),
    path('login/', Login_view.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('AddDevice/', views.AddDevice, name='AddDevice'),
    path('Add/', views.AddQuestion, name='AddQuestion'),
    path('FAQ/', views.faq, name='faq'),
    path('Reservation/', views.Reservation, name='Reservation'),
    path('student_interface/', views.student_interface, name='student_interface'),
    path('experiment/', views.Experiment, name='Experiment'),
    path('Pricing/', views.Plan, name='Pricing'),
    path('AddPlan/', views.AddPlan, name='AddPlan'),
    path('Contact_Us/', views.Contact_Us, name='Contact_Us'),



]
