from dashboard.models import Test
from django.db import models


class Result(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    correct_answers = models.IntegerField(blank=False, null=False)
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Test: {self.test.id}"
