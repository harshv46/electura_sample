from django.db import models

# Create your models here.

class tasks(models.Model):
    creator = models.CharField(max_length= 100)
    desc = models.CharField(max_length= 1000)
    completed = models.BooleanField(default = False)