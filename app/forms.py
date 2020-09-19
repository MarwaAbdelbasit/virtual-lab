from django import forms
from . import models
from virtualLab import settings

class AccountsForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = models.Accounts
        fields = ('email', 'username', 'phone', 'university', 'faculty', 'date_of_birth', 'country', 'password', 'user_type')
