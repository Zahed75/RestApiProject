from django.conf.urls import url
from django.urls import path
from MainApp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('post_student/',views.post_data,name='post_data'),
    path('update-student/<id>',views.update_student,name='changed'),
]