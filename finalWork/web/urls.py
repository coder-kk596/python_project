from django.conf.urls import url
from lib import views


urlpatterns = [
    url('movies/', views.index, name='index'),
    url('phones/', views.index, name='phones'),
    url('houses/', views.index, name='houses'),
    url('articles/', views.index, name='articles'),
]
