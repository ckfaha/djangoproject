from django.contrib import admin
from django.urls import path
from modelapp import views

urlpatterns = [
    path('get/',views.EmployeeDetails),
    path('create/',views.createemployee),
    path('sample/',views.sampleForm),
    path('search/',views.searchitems),



]