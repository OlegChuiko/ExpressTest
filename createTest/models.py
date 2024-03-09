from django.db import models


# Create your models here.

class Test(models.Model):
    file = models.FileField(upload_to='uploads/')
    unique_code = models.CharField(max_length=6, unique=True)

    def __code__(self):
        return self.unique_code