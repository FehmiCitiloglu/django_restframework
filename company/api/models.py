from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=11, decimal_places=2)
    location = models.CharField(max_length=125)
