from django.conf.urls import url
from django.urls import path
from MainApp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('post_student/',views.post_data,name='post_data'),
    path('update-student/<id>',views.update_student,name='changed'),
    path('delete_student/<id>',views.delete_student,name='delete'),
    path('book_list/',views.get_book,name='book_list'),
    path('register/',views.RegisterUser.as_view()),
]