import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FirstProject.settings')

import django
django.setup()

from CrudApp.models import Employee
from faker import Faker
from random import randint
fake=Faker()
def generatefakedata():
    f_name=fake.name()
    f_phno=randint(600000000,999999999)
    f_age=randint(18,99)
    f_email=fake.email()
    f_city=fake.city()
    Employee.objects.get_or_create(name=f_name,
                                   pho=f_phno,
                                   age=f_age,
                                   email=f_email,
                                   city=f_city)



for i in range(0,11,1):
    generatefakedata()