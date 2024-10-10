from django.contrib import admin
from django.urls import path
from SecondApplication import views

urlpatterns = [
    path('second/',views.secondapp),
    path('ipl/',views.ipltable),
    path('price/',views.price),
    path('total/',views.total),



]