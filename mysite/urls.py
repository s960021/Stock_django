from os import name
from django.contrib import admin
from django.urls import path
from trips.views import *


urlpatterns = [
    path('', ad,name='index'),
    path('our/', our)
]
