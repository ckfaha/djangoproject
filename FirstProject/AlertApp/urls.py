from django.contrib import admin
from django.urls import path
from AlertApp import views

urlpatterns = [
    path('sample/',views.samplealert),
    path('success/', views.success,name="success"),
    path('error/', views.error,name="error"),
    path('warning/', views.warning,name="warning"),
    path('info/', views.info,name="info"),




]