from django.urls import path
from main import views


app_name = 'main'

urlpatterns = [
    path('',views.Main.index,name='index'),
]