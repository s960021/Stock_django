from django.contrib import admin
from django.urls import path
from trips.views import ad


urlpatterns = [
    path('',ad)

]
