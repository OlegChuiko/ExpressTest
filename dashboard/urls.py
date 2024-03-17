from django.contrib import admin
from django.urls import path
from dashboard import views


app_name = 'dashboard'

urlpatterns = [
   path('',views.dashboard,name='dashBoard'),
   path('create_test/',views.createTest,name='createTest'),
   path('create_test/unique_code_for_test/<str:unique_code>/', views.unique_codeForTest, name='unique_codeForTest')
]