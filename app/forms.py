# accounts.forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.conf import settings
from .models import *
import datetime

User = get_user_model()

class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'email', 'university', 'faculty', 'date_of_birth', 'type',) # if you have more fields that email and password

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'university', 'faculty', 'date_of_birth', 'active', 'admin', 'type',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class RegisterForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = User
        fields = ('full_name', 'email', 'university', 'faculty', 'date_of_birth', 'type',) # if you have more fields that email and password

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # user.active = False #send confirmation email
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)


# add devices form
class AddDeviceForm(forms.ModelForm):
    # description = forms.CharField(widget=forms.Textarea,max_length=4000)

    class Meta:
        model = Devices
        fields = ('name', 'status', 'description', 'rate', 'review', 'category', 'image')


# add question form
class AddQForm(forms.ModelForm):
    # Question = forms.CharField(widget=forms.PasswordInput)
    Answer = forms.CharField(widget=forms.Textarea,max_length=4000)

    class Meta:
        model = FAQ
        fields = ('Question', 'Answer')


# add Reservation form
class ReserveForm(forms.ModelForm):
    Start_time = forms.DateTimeField(initial=datetime.date.today)
    Finish_time = forms.DateTimeField(initial=datetime.date.today)
    class Meta:
        model = Reservation
        fields = ('Device', 'Start_time', 'Finish_time')



# experiment form
class ExperimentsForm(forms.ModelForm):
    class Meta:
        model = Experiments
        fields = ('title', 'description', 'experiment_id', 'device_name', 'duration')



# Pricing form
class PricingForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('plan_name', 'price', 'feauters_of_plan')


# ContactUs form
class Contact_UsForm(forms.ModelForm):
    class Meta:
        model = Contact_Us
        fields = ('Subject', 'Message')


# AddPlan form
class AddPlan(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('plan_name', 'price', 'feauters_of_plan', 'number_of_coupons')


# add coupon form
class AddCouponForm(forms.ModelForm):
    code = forms.CharField(max_length=4000)
    class Meta:
        model = Coupon
        fields = ('code', 'active')

# apply coupon form
class ApplyCouponForm(forms.ModelForm):
    code = forms.CharField()
    class Meta:
        model = Coupon
        fields = ('code',)


# purchase a plan form
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('plan_name', 'payment_option')
