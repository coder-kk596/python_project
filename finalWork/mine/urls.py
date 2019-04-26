from django.conf.urls import url
from mine import views


urlpatterns = [
    url('index/', views.index, name='index'),
    url('test',views.test),
    url('table/',views.detail, name='detail')
]
