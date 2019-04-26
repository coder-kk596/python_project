from django.urls import path
from lib import views


urlpatterns=[
    path('table/',views.detail, name='detail')
]