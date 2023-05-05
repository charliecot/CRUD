from django.db import models
from django.urls import reverse

# Create your models here.
class  Student(models.Model):
    name= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    matricule= models.CharField(max_length=100)
    level= models.IntegerField()



