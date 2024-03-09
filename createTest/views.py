import random
import string
from django.core.files.storage import FileSystemStorage
from django.db import transaction
from .models import Test
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def unique_codeForTest(request,unique_code):
    return render(request,'main/unique_codeForTest.html',{'unique_code': unique_code})


def createTest(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        unique_code = None
        while True:
            # Генеруємо унікальний шестизначний код
            unique_code = ''.join(random.choices(string.digits, k=6))
            
            # Перевіряємо, чи не існує вже запису з таким унікальним кодом
            if not Test.objects.filter(unique_code=unique_code).exists():
                break


        # Зберігаємо у базі даних
        with transaction.atomic():
            model_instance = Test(file=myfile, unique_code=unique_code)
            model_instance.save()

        return redirect('createTest:unique_codeForTest',unique_code = unique_code)  # Перенаправлення на сторінку з кодом

    return render(request, 'main/create_test.html')