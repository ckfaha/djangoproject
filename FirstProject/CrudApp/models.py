from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=15)
    pho=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
    city=models.CharField(max_length=15)


    def __str__(self):
        return self.name