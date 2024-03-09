from django.contrib import admin
from django.urls import path
from createTest import views


app_name = 'createTest'

urlpatterns = [
   path('',views.createTest,name='createTest'),
   path('unique_code_for_test/<str:unique_code>/', views.unique_codeForTest, name='unique_codeForTest')
]