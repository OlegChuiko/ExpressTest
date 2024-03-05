from django.shortcuts import render

# Create your views here.

def createTest(request):
    return render(request,'main/create_test.html')