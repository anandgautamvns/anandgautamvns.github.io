from django import forms
from django.contrib.auth.models import User
from login.models import UserProfileInfoForm


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    portfolio_site = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta():
        model = UserProfileInfoForm
        fields = ('portfolio_site','profile_pic')
