from django.urls import path
from dashboard import views


app_name = 'dashboard'

urlpatterns = [
   path('',views.Dashboard.dashboard,name='dashBoard'),
   path('test/<int:test_id>/',views.TestParameters.test_parameters,name='test_parameters'),
   path('create_test/',views.CreateTest.create_test,name='createTest'),
   path('delete_test/', views.Delete.DeleteTest, name='delete_test'),
   path('create_test/unique_code_for_test/<str:unique_code>/', views.UniqueCode.unique_codeForTest, name='unique_codeForTest')
]