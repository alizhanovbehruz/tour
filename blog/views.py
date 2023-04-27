from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def packk(request):
    post = Tickets.objects.all()
    context = {
        'post': post
    }
    return render(request,'packages.html',context=context)

def pack_show(request,post_id):
    post = Tickets.objects.get(pk=post_id)
    context = {
        'post':post
    }
    return render(request,'tour_id.html',context=context)


def hotels(request):
    return render(request,'hotels.html')

def contact(request):
    post = Contacts.objects.get(pk=1)
    context = {
        'post':post
    }
    return render(request,'contact.html',context=context)