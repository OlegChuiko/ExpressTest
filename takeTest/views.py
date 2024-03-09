from django.shortcuts import render
from django.http import HttpResponse
from createTest.models import Test

# Create your views here.
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
                if line != '\n':  # Ця умова ігнорує порожні рядки
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
        return HttpResponse('Не вказано код доступу до тесту')

   

    return render(request, 'main/test.html', {'qas': zip(questions, answers)})