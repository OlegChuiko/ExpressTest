from dashboard.models import Test
from django.db import models


class Result(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False,verbose_name='Ім\'я')
    last_name = models.CharField(max_length=255, blank=False, null=False,verbose_name='Прізвище')
    correct_answers = models.IntegerField(blank=False, null=False,verbose_name='Правильні відповіді')
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False,verbose_name='Оцінка')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, blank=False, null=False,verbose_name='Тест')

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результати"


    def __str__(self):
        return f"{self.first_name} {self.last_name} - Тест: {self.test.id}"
