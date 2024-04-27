from users.models import User
from django.db import models
import os


class Test(models.Model):
    test_name = models.CharField(max_length=255, blank=False, null=False,default=None,verbose_name='Назва тестування')
    file = models.FileField(upload_to='uploads/',verbose_name='Файл з тестуванням')
    unique_code = models.CharField(max_length=6, unique=True,verbose_name='Унікальний код')
    duration_test = models.IntegerField(default=0,verbose_name='Тривалість тестування(хв)')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, default=None,verbose_name='Користувач')
    test_date = models.DateField(auto_now_add=True,blank=False, null=False,verbose_name='Дата створення')

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тести"


    def filename(self):
        return os.path.basename(self.file.name)

    def __code__(self):
        return self.unique_code

    def __str__(self):
     return f"Тест ({self.id}, {self.user_id.username})"

    