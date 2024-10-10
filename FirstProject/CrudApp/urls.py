from django.contrib import admin
from django.urls import path
from CrudApp import views

urlpatterns = [
    path('get/',views.getemployee,name="get"),
    path('create/',views.createemployee,name="create"),
    path('delete/<id>',views.deleteuser,name="deleteuser"),
    path('update/<id>',views.updateemployee,name="updateuser"),
    path('login/',views.loginpage,name="loginpage"),
    path('logout/',views.logoutuser,name="logout"),
    path('signup/',views.registeruser,name="signup")



]