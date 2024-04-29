from django.views.decorators.cache import never_cache
from django.shortcuts import redirect, render
from django.http import HttpResponse
from dashboard.models import Test
from .models import Result
import os

class InputCode:
    def takeTest(request):
        request.session['isTesting'] = True
        return render(request,'main/take_test.html')

class Testing:
    @never_cache
    def test(request):
        if request.session.get('isTesting') == True:
            unique_code = request.POST.get('accessCode',None)
            first_name = request.POST.get('first_name',None)
            last_name = request.POST.get('last_name',None)
            error = None

            if unique_code:
                try:
                    # Отримуємо модель за унікальним ключем
                    TestFile = Test.objects.get(unique_code=unique_code)
                    if not os.path.exists(TestFile.file.path):
                        return HttpResponse('Файл не знайдено')
                except Test.DoesNotExist:
                     error = "Тестування не знайдено"
                     return render(request,'main/take_test.html',{'first_name' : first_name,'last_name' : last_name,'errorCode' : error,'unique_code' : unique_code})
                
                questions = []
                answers = []

                isQuestion = False

                with open(TestFile.file.path, "r", encoding="utf-8") as f:
                    for line in f:
                        # Перевірка, чи рядок не є порожнім
                        if line != '\n':  
                            if not isQuestion:
                                questions.append(line.strip())
                                isQuestion = True
                            else:
                                tempAnswers = []
                                tempVal = line.strip()
                                tempAnswers.append(tempVal)
                                for temp_line in f:
                                    if temp_line == '\n':
                                        break
                                    tempAnswers.append(temp_line.strip())
                                answers.append(tempAnswers)
                                isQuestion = False


            # Зберігаємо дані у сеансі
            request.session['questions'] = questions
            request.session['answers'] = answers
            request.session['first_name'] = first_name
            request.session['last_name'] = last_name
            request.session['unique_code'] = unique_code

            test_duration = TestFile.duration_test
            
            
            return render(request, 'main/test.html', {'qas': zip(questions, answers),'test_duration': test_duration})
        else:
            return redirect('main:index')
   
class Results:       
    def TestResult(request):

        if request.method == 'POST':
            user_answers = []
            for key, value in request.POST.items():
                if key.startswith('UserAnswer'):
                    user_answers.append(value)
                
            # Витягуємо дані з сеансу
            questions = request.session.get('questions', [])
            answers = request.session.get('answers', [[]])

            first_name = request.session.get('first_name')
            last_name = request.session.get('last_name')
            unique_code = request.session.get('unique_code')

            #Логіка визначення результатів тут
            total_questions = len(questions)
            correct_answers = sum(1 for user_answer in user_answers if user_answer[-1]=='+')
            incorrect_answers = total_questions - correct_answers

            ratio = correct_answers / total_questions
            grade = round(ratio * 5,2)

            #Записуєм дані в базу
            test = Test.objects.get(unique_code=unique_code)

            result = Result(first_name=first_name,last_name=last_name,correct_answers=correct_answers,grade=grade,test=test)
            result.save()

            request.session['isTesting'] = False

            return render(request,'main/test_results.html',{'qas' : zip(questions,answers,user_answers),'total_questions' : total_questions,
            'correct_answers' : correct_answers,'incorrect_answers' : incorrect_answers,'grade' : grade}) 

    
