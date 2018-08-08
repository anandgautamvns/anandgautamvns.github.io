from django.shortcuts import render,render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import *
from .models import *
from .form import *
# Create your views here.

#image upload
'''
def gallery(request):
    img=Upload.objects.all()
    return render(request,'gallery.html',{"img":img})

'''


def upload_product(request):
    if request.POST:
        form =uploadform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('upload_product')

    else:
        form=uploadform()
    return render(request,'seller/upload.html',{'form':form})
