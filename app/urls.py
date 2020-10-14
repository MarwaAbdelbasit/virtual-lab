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
    path('addCoupon/', views.addCoupon, name='coupon'),
    path('addPlan/', views.addPlan, name='addPlan'),
    path('Pricing/', views.Plan_view, name='Pricing'),
    path('purchase/', views.purchase_view, name='purchase'),
    path('getCoupons/', views.getCoupon, name='getcoupon'),
    path('applyCoupon/', views.apply_coupon, name='applyCoupon'),
    path('workSpace/', views.work_space_view, name='workSpace'),
    path('Contact_Us/', views.Contact_Us, name='Contact_Us'),
]
