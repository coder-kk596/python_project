# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from final.models import Doubanmoviesall,Phonejd,House,Wechatessays
from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index_.html')

def movie(request):
    movies_list=Doubanmoviesall.objects.all()
    context={'movielist':movies_list}
    print(context)
    return render(request,'movies.html',context)

def phone(request):
    phone_list=Phonejd.objects.all()
    context={'phonelist':phone_list}
    print(context)
    return render(request,'phones.html',context)

def house(request):
    house_list=House.objects.all()
    context={'houselist':house_list}
    print(context)
    return render(request,'houses.html',context)

def article(request):
    articles_list=Wechatessays.objects.all()
    context={'articlelist':articles_list}
    print(context)
    return render(request,'articles.html',context)
