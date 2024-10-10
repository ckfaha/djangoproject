from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,r"firstapp/first.html")
def home(request):
    msg="""
    <head>
    <title>|Homepage
    </title>
    </home>
    <body>
    <h1 >My Application Homepage</h1>
    </body>
    </html>"""
    return HttpResponse(msg)
def login(request):
    msg="""
    <head>
    <title>|Login
    </title>
    </home>
    <body>
    <h1 >My Application LoginPage</h1>
    </body>
    </html>"""
    return HttpResponse(msg)
def register(request):
    msg="""
    <head>
    <title>|Register
    </title>
    </home>
    <body>
    <h1 >My Application RegisterPage</h1>
    </body>
    </html>"""
    return HttpResponse(msg)