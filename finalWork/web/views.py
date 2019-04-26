# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lib.models import Moviesdouban

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'test.html')

def detail(request):
    movies_list=Moviesdouban.objects.all()
    context={'movielist':movies_list}
    print(context)
    return render(request,'detail.html',context)
