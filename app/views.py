from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import CreateView, FormView
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from . import forms
from .forms import RegisterForm, LoginForm, AddDeviceForm, AddQForm, ReserveForm, ExperimentsForm, AddCouponForm, AddPlan, PricingForm, PurchaseForm, ApplyCouponForm, Contact_UsForm
from django.contrib.auth import login, logout
from .models import  *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def student_interface(request):
    return render(request, 'app/student_interface.html')

def devices(request):
    devices = Devices.objects.all()
    experiments = Experiments.objects.all()
    return render(request, 'app/devices.html', {'devices':devices,
    'experiments': experiments})

class Register_view(CreateView):
    form_class = RegisterForm
    template_name = 'app/register.html'
    success_url = '/'

class Login_view(FormView):
    form_class = LoginForm
    # success_url = '/home.html'
    template_name = 'app/login.html'

    def form_valid(self, form):
        request = self.request

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            success_url = '/'
            next_ = request.GET.get('next')
            next_post = request.POST.get('next')
            redirect_path = next_ or next_post or success_url or None
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(Login_view, self).form_invalid(form)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required(login_url='/app/login/')
def AddDevice(request):
    if request.method == 'POST':
        form = AddDeviceForm(request.POST)
        if form.is_valid():
            # save account to database
            form.save()
            return redirect('home')
    else:
        form = AddDeviceForm()
    return render(request, 'app/AddDevice.html', {'form': form})

@login_required(login_url='/app/login/')
def AddQuestion(request):
    if request.method == 'POST':
        form = AddQForm(request.POST)
        if form.is_valid():
            # save account to database
            form.save()
            return redirect('home')
    else:
        form = AddQForm()
    return render(request, 'app/AddQ.html', {'form': form})


def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'app/FAQ.html', {'faqs':faqs})


@login_required(login_url='/app/login/')
def Reservation(request):
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            # save account to database
            instance_of_reservation = form.save(commit=False)
            # commit=False: means hang on a minute we are going to save this but don't commit to the action yet
            instance_of_reservation.user = request.user
            # user on left of the equal sign refers to the user data field in reservation model
            instance_of_reservation.save()
            return redirect('home')
    else:
        form = ReserveForm()
    return render(request, 'app/Reserve.html', {'form': form})


@login_required(login_url='/app/login/')
def Experiment(request):
    if request.method == 'POST':
        form = ExperimentsForm(request.POST)
        if form.is_valid():
            # save experiment to db
            instance_of_experiment = form.save(commit=False)
            instance_of_experiment.user_exp = request.user
            instance_of_experiment.save()
            return redirect('app:workSpace')
    else:
        form = ExperimentsForm()
    return render(request, 'app/experiment.html', {'form': form})


def addCoupon(request):
    if request.method == 'POST':
        form = AddCouponForm(request.POST)
        if form.is_valid():
            # save coupon to db
            form.save()
            messages.info(request, 'Your coupon has been saved successfully!')
    else:
        form = AddCouponForm()
    return render(request, 'app/addCoupon.html', {'form': form})

def addPlan(request):
    if request.method == 'POST':
        form = AddPlan(request.POST)
        if form.is_valid():
            # save coupon to db
            form.save()
            messages.info(request, 'Your plan has been saved successfully!')
    else:
        form = AddPlan()
    return render(request, 'app/addPlan.html', {'form': form})


#View of pricing
def Plan_view(request):
   Plans = Plan.objects.all()
   return render(request, 'app/Pricing.html', {'Plans':Plans})


# purchase view
def purchase_view(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            # save order to db
            instance_of_purchase = form.save(commit=False)
            instance_of_purchase.institute = request.user
            request.paid = True
            instance_of_purchase.save()
            messages.info(request, 'Your order has been saved successfully!')
    else:
        form = PurchaseForm()
    return render(request, 'app/purchase.html', {'form': form})

def getCoupon(request):
    coupons = Coupon.objects.all()
    # purchases = Purchase.objects.filter(institute = User.email)
    return render(request, 'app/getCoupon.html', {'coupons': coupons})


def apply_coupon(request):
    # if request.method == 'GET':
    form  = ApplyCouponForm(request.GET)
    #     if form.is_valid():
    code_entered = request.GET.get('code')
    coupon = Coupon.objects.filter(code = code_entered).first()
    is_available = True if coupon else False
    is_active = coupon.active if coupon else False
    if is_available and is_active:
        # messages.info(request, 'Your coupon is verified!')
        return redirect('app:student_interface')
    # else:
    #     form = ApplyCouponForm()
    return render(request, 'app/applyCoupon.html', {'form': form})

def work_space_view(request):
    return render(request, 'app/work_space.html')

#View of Contact us
def Contact_Us(request):
    if request.method == 'POST':
        form = Contact_UsForm(request.POST)
        if form.is_valid():
            # save account to database
            form.save()
            return redirect('home')
    else:
        form = Contact_UsForm()
    return render(request, 'app/Contact_Us.html', {'form': form})
