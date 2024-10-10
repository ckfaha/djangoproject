from django.db import models

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=30)
    empid=models.IntegerField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    studentname=models.CharField(max_length=20)
    studentId=models.IntegerField()
    studentsection=models.CharField(max_length=30)
    studentmark=models.IntegerField()

    class Meta:
        ordering=["studentname"]

    def __str__(self):
        return self.studentname

class School(Student):
    schoolname=models.CharField(max_length=100)


    def __str__(self):
        return self.schoolname

