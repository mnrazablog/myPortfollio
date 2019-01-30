from django.urls import path, include
from . import views

urlpatterns = [
   
    path('',views.allblogs,name='allblogs'),
    path('<int:blog_id>/',views.blog_details,name='blogdetails'),
   
] 