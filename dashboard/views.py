from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from users.forms import ProfileForm
from django.shortcuts import render
from takeTest.models import Result
from django.db import transaction
from users.models import User
from .models import Test
import random
import string
import os

class UniqueCode:
    @login_required
    def unique_codeForTest(request,unique_code):
        return render(request,'main/unique_codeForTest.html',{'unique_code': unique_code})

class CreateTest:
    @login_required
    def create_test(request):
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']

            unique_code = None
            while True:
                # Генеруємо унікальний шестизначний код
                unique_code = ''.join(random.choices(string.digits, k=6))
                
                # Перевіряємо, чи не існує вже запису з таким унікальним кодом
                if not Test.objects.filter(unique_code=unique_code).exists():
                    break

            # Отримання часу тестування та назву з POST-запиту
            duration_test = request.POST.get('duration_test')
            test_name = request.POST.get('test_name')

            user_id = request.user.id
            user = User.objects.get(id=user_id)

            error = None
            filename = myfile.name
            if not filename.endswith('.txt'):
                error = 'Некоректний формат файлу'
                return render(request, 'main/create_test.html',{'test_name':test_name,'errorFile': error})
            elif myfile.size == 0:
                error = "Файл порожній"
                return render(request, 'main/create_test.html',{'test_name':test_name,'errorFile': error})

            # Зберігаємо у базі даних
            with transaction.atomic():
                model = Test(test_name=test_name,file=myfile, unique_code=unique_code,duration_test=duration_test,user_id=user)
                model.save()

            return redirect('dashboard:unique_codeForTest',unique_code = unique_code)  

        return render(request, 'main/create_test.html')

class Dashboard:
    @login_required
    def dashboard(request):
        form = ProfileForm(instance=request.user)

        user_id = request.user.id
        user_tests = Test.objects.filter(user_id=user_id).order_by('-test_date')

        return render(request,'main/dashboard.html',{'form':form,'user_tests':user_tests})

class TestParameters:
    @login_required
    def test_parameters(request,test_id):

        test = get_object_or_404(Test, id=test_id)
        if request.method == 'POST':
            if request.POST.get('newTestName'):
                new_test_name = request.POST.get('newTestName')
                test.test_name = new_test_name
                test.save()
            elif request.POST.get('newDuration'):
                new_test_duration = request.POST.get('newDuration')
                test.duration_test = new_test_duration
                test.save()
            elif request.FILES.get('NewTest'):
                new_test = request.FILES['NewTest']
                test.file = new_test
                test.save()

        filename = test.filename()
        results = Result.objects.filter(test=test)

        form = ProfileForm(instance=request.user)

        user_id = request.user.id
        user_tests = Test.objects.filter(user_id=user_id).order_by('-test_date')

        return render(request,'main/test_parameters.html',{'test':test,'filename':filename,'results':results,'form':form,'user_tests':user_tests})

class Delete:
    @login_required
    def DeleteTest(request):
        if request.method == 'POST':
            test_id = request.POST.get('test_id')
            if test_id:
                test = get_object_or_404(Test, id=test_id)

                if os.path.exists(test.file.path):
                    os.remove(test.file.path)

                test.delete()
                return redirect('dashboard:dashBoard')
