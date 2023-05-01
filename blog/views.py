from django.shortcuts import render
from .models import *
# Create your views here.
from django.http import HttpResponseRedirect
from .forms import Ticket1
from django.db.models import Q


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
        'i':post
    }
    return render(request,'tour_id.html',context=context)


def hotels(request):
    form = Ticket1
    posts = aviatickets.objects.all()
    search_query = request.GET.get('fly_to','')
    context = {
        'posts':posts,
        'lis':[],
        "form":form,
    }
    return render(request,'hotels.html',context=context)


def filter_tick(request):
    search_query_from = request.GET.get('fly_from','')
    search_query_to = request.GET.get('fly_to','')
    search_query_date = request.GET.get('date','')
    search_query_per = request.GET.get('per','')

    if search_query_from or search_query_to :
        posts = aviatickets.objects.filter(fly_from__icontains=search_query_from, fly_to__icontains=search_query_to)
        if search_query_date:
            posts = posts.filter(date=search_query_date)
    else:
        posts = aviatickets.objects.all()
    context = {
        'posts':posts
    }

    return render(request,'filter_tickk.html',context=context)


def contact(request):
    post = Contacts.objects.get(pk=1)
    context = {
        'post':post
    }
    return render(request,'contact.html',context=context)