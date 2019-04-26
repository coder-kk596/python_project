from django.conf.urls import url
from final import views


urlpatterns = [
    url(r'^index/', views.index, name='my_index'),
    url(r'^movies/', views.movie, name='my_movies'),
    url('phones/', views.phone, name='my_phones'),
    url('houses/', views.house, name='my_houses'),
    url('articles/', views.article, name='my_articles'),
]