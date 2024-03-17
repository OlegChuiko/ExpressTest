from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from users.forms import ProfileForm
from django.shortcuts import render
from django.db import transaction
from .models import Test
import random
import string


@login_required
def unique_codeForTest(request,unique_code):
    return render(request,'main/unique_codeForTest.html',{'unique_code': unique_code})

@login_required
def createTest(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        #filename = fs.save(myfile.name, myfile)

        unique_code = None
        while True:
            # Генеруємо унікальний шестизначний код
            unique_code = ''.join(random.choices(string.digits, k=6))
            
            # Перевіряємо, чи не існує вже запису з таким унікальним кодом
            if not Test.objects.filter(unique_code=unique_code).exists():
                break

        # Отримання часу тестування з POST-запиту
        duration_test = request.POST.get('duration_test')

        # Зберігаємо у базі даних
        with transaction.atomic():
            model = Test(file=myfile, unique_code=unique_code,duration_test=duration_test)
            model.save()

        return redirect('dashboard:unique_codeForTest',unique_code = unique_code)  # Перенаправлення на сторінку з кодом

    return render(request, 'main/create_test.html')

@login_required
def dashboard(request):
    form = ProfileForm(instance=request.user)

    return render(request,'main/dashboard.html',{'form':form})

