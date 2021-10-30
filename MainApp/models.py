from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=444)
    age=models.IntegerField(default=18)
    department=models.CharField(max_length=44)
    location=models.CharField(max_length=44)