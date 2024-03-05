from django.contrib import admin
from django.urls import path
from createTest import views


app_name = 'createTest'

urlpatterns = [
   path('',views.createTest,name='createTest'),

]