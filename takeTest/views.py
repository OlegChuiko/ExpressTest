from dashboard.models import Test
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse


def takeTest(request):
    return render(request,'main/take_test.html')

def test(request):

    unique_code = request.GET.get('accessCode',None)

    if unique_code:
        try:
            # Отримуємо модель за унікальним ключем
            TestFile = Test.objects.get(unique_code=unique_code)
        except Test.DoesNotExist:
            return HttpResponse('Файл не знайдено')
        
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
    else:
        return HttpResponse('Не вказано код доступу до тесту')#Виправити щоб не можна було відправити пусту строку з кодом

    # Зберігаємо дані у сеансі
    request.session['questions'] = questions
    request.session['answers'] = answers

    test_duration = TestFile.duration_test

    return render(request, 'main/test.html', {'qas': zip(questions, answers),'test_duration': test_duration})


def TestResult(request):

    if request.method == 'POST':
        user_answers = []
        for key, value in request.POST.items():
            if key.startswith('UserAnswer'):
                user_answers.append(value)
            
        # Витягуємо дані з сеансу
        questions = request.session.get('questions', [])
        answers = request.session.get('answers', [[]])

        #Логіка визначення результатів тут
        total_questions = len(questions)
        correct_answers = sum(1 for user_answer in user_answers if user_answer[-1]=='+')

        ratio = correct_answers / total_questions
        grade = round(ratio * 5,2)

        return render(request,'main/test_results.html',{'qas' : zip(questions,answers,user_answers),'total_questions' : total_questions,
        'correct_answers' : correct_answers,'grade' : grade}) 

    
