from django.shortcuts import render,render_to_response, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def profile(request):
    username = UserProfileInfo.objects.all().filter(user=request.user)
    print (request.user)
    return render(request,'profile.html',{'username':username})

@login_required
def special(request):
    return HttpResponse('You are login, Nice')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def registration(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():
            print ("Hello")
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'registration.html',
                            { 'user_form':user_form,
                             'profile_form':profile_form,
                             'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('Account Not Active')
        else:
            print('some try to login and failed!')
            print("username:{} and password:{}".format(username,password))
            return HttpResponse('Invalid Login Details supplied')
    else:
        return render(request,'login.html')
