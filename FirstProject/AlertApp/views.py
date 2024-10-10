from django.contrib import messages
from django.shortcuts import render

# Create your views here.
def samplealert(request):
    return render(request,"alertapp/messageapp.html")

def success(request):
    messages.success(request,"this is success message")
    return render(request,"alertapp/messageapp.html")

def error(request):
    messages.error(request,"this is error message")
    return render(request,"alertapp/messageapp.html")

def warning(request):
    messages.warning(request,"this is warning message")
    return render(request,"alertapp/messageapp.html")

def info(request):
    messages.info(request,"this is info message")
    return render(request,"alertapp/messageapp.html")