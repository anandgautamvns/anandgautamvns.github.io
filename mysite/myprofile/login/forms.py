from django import forms
from django.contrib.auth.models import User
from .models import *


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    portfolio_site = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    employee_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    department = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta():
        model = UserProfileInfo
        fields = '__all__'
