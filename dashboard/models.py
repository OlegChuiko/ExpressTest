from users.models import User
from django.db import models
import os


class Test(models.Model):
    test_name = models.CharField(max_length=255, blank=False, null=False,default=None)
    file = models.FileField(upload_to='uploads/')
    unique_code = models.CharField(max_length=6, unique=True)
    duration_test = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, default=None)
    
    def filename(self):
        return os.path.basename(self.file.name)

    def __code__(self):
        return self.unique_code

    