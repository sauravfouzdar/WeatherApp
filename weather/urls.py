from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('delete/<city_name>', views.remove_city,name='remove_city'),
]































