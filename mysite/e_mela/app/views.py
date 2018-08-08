from django.shortcuts import render
from django.http import *
from seller.models import uploadItem
# Create your views here.

def home(request):
    return render(request, 'home.html')

def electronics(request):
    products = uploadItem.objects.all().filter(product_category='Electronics')
    #print (products)
    return render(request,'electronics.html',{'products':products})

def restaurants(request):
    products = uploadItem.objects.all().filter(product_category='Restaurants')
    return render(request,'restaurants.html',{'products':products})


def sports(request):
    products = uploadItem.objects.all().filter(product_category='Sports')
    return render(request,'sports.html',{'products':products})

def automobiles(request):
    products = uploadItem.objects.all().filter(product_category='Automobiles')
    return render(request,'automobiles.html',{'products':products})
