from django.http import HttpResponse
from django.shortcuts import render
from .models import empdet
from django.db.models import Q
from .forms import EmployeeForm, FormClass


# Create your views here.
def EmployeeDetails(request):
    employees=empdet.objects.all()
    return render(request,"modelapp/alldata.html",context={"employees":employees})

def createemployee(request):
    if(request.method=="POST"):
        if(request.POST.get("employeeid") and request.POST.get("username")
                and request.POST.get("age") and request.POST.get("phno")):
            register=empdet()
            register.empid=request.POST.get("employeeid")
            register.name=request.POST.get("username")
            register.age=request.POST.get("age")
            register.pho=request.POST.get("phno")
            register.save()
            return HttpResponse("<h2>Successfully Stored <a href='/model/get'>Click Here</a>to redirect Homepage</h2>")
        else:
            return HttpResponse("Some fields are missing,Please fill the details")
    forms=EmployeeForm()
    return render(request,"modelapp/EmployeeForm.html",context={"forms":forms})




def sampleForm(request):
     form=FormClass()
     return render(request,"modelapp/FormField.html",context={"form":form})


def searchitems(request):
    srch=request.GET.get("search")
    emp_count=0
    if srch:
        employees=empdet.objects.filter(Q(name__icontains=srch) | Q (empid__icontains=srch))
        emp_count=employees.count()

    else:
        employees=empdet.objects.all()
        emp_count=employees.count()
    return render(request, "modelapp/alldata.html", context={"employees": employees})
