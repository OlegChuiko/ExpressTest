from django.contrib import admin
from django.urls import path
from takeTest import views


app_name = 'takeTest'

urlpatterns = [
   path('',views.InputCode.takeTest,name='takeTest'),
   path('test/',views.Testing.test,name='test'),
   path('test/result',views.Results.TestResult,name='testResult'),
]