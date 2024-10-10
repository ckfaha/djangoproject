from django.db import models

# Create your models here.
class empdet(models.Model):
    empid=models.IntegerField()
    age=models.IntegerField(max_length=2)
    name=models.CharField(max_length=20)
    pho=models.IntegerField(max_length=10)

    def __str__(self):
        return self.name
