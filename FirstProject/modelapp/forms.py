from django import forms
from django.core.validators import MinValueValidator


class EmployeeForm(forms.Form):
    employeeid=forms.IntegerField()
    username=forms.CharField(max_length=20)
    age=forms.IntegerField()
    phno=forms.IntegerField()

class FormClass(forms.Form):
    name=forms.CharField(min_length=3,max_length=20,required=True,initial="enter name:",label="Full Name")
    password=forms.CharField(min_length=4,max_length=16,widget=forms.PasswordInput())
    age=forms.IntegerField(min_value=18,max_value=40,initial=18,)