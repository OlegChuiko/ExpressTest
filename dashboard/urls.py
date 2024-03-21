from django.contrib import admin
from django.urls import path
from dashboard import views


app_name = 'dashboard'

urlpatterns = [
   path('',views.dashboard,name='dashBoard'),
   path('test/<int:test_id>/',views.test_parameters,name='test_parameters'),
   path('create_test/',views.createTest,name='createTest'),
   path('delete_test/', views.DeleteTest, name='delete_test'),
   path('create_test/unique_code_for_test/<str:unique_code>/', views.unique_codeForTest, name='unique_codeForTest')
]