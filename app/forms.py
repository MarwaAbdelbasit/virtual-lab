from django import forms
from . import models

class AddQuestion(forms.ModelForm):
	class Meta:
        model = models.faq
        fields = ('Question', 'Answer')
class AddDevice(forms.ModelForm):
	class Meta:
        model = models.Devices
        fields = ('name', 'description', 'category', 'image', 'status')