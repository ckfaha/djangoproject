from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def secondapp(request):
    return HttpResponse("THis is second application")
def ipltable(request):
    d=datetime.now()
    return render(request,r"secondapp/table.html",context={"date":d})
def price(request):

    return render(request,r"secondapp/price.html")
def total(request):
    mobile=int(request.GET["mob"])
    laptop=int(request.GET["lap"])
    keyboard=int(request.GET["key"])
    mouse=int(request.GET["mou"])
    tv=mobile+laptop+keyboard+mouse
    return render(request,r"secondapp/totalprice.html",context={"value":tv})