from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=444)
    age = models.IntegerField(default=18)
    department = models.CharField(max_length=44)
    location = models.CharField(max_length=44)


class category(models.Model):
    category_name = models.CharField(max_length=444)

    def __str__(self):
        return self.category_name


class Book(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=44)
