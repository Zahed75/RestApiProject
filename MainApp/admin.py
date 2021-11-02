from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','department','age','location')


@admin.register(category)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','book_title')