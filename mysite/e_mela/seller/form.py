from django import forms
from .models import *
from .choices import *

class uploadform(forms.ModelForm):
    product_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))
    discount = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    product_category = forms.ChoiceField(choices=STATUS_CHOICES,initial='',widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model=uploadItem
        fields='__all__'
