from django.db import models


class Test(models.Model):
    file = models.FileField(upload_to='uploads/')
    unique_code = models.CharField(max_length=6, unique=True)
    duration_test = models.IntegerField(default=0)

    def __code__(self):
        return self.unique_code