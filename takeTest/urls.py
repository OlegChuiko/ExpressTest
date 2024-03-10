from django.contrib import admin
from django.urls import path
from takeTest import views


app_name = 'takeTest'

urlpatterns = [
   path('',views.takeTest,name='takeTest'),
   path('test/',views.test,name='test'),
   path('test/result',views.TestResult,name='testResult'),
   
]