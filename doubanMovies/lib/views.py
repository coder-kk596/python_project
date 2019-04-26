from django.shortcuts import render
from lib.models import Moviesdouban


# Create your views here.
def detail(request):
    movies_list=Moviesdouban.objects.all()
    context={'movielist':movies_list}
    print(context)
    return render(request,'detail.html',context)
