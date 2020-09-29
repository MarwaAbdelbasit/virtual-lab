from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import CreateView, FormView
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from . import forms
from .forms import RegisterForm, LoginForm, AddDeviceForm, AddQForm,ReserveForm
from django.contrib.auth import login, logout
from .models import  *
from django.contrib.auth.decorators import login_required

# Create your views here.
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
    success_url = '/app/devices.html'
    template_name = 'app/login.html'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
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
        return redirect('/')

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
