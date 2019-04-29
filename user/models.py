
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.



class Person(models.Model):
    name = models.CharField(max_length = 15)
    publishtime = models.DateTimeField(default = 0)
    location = models.CharField(max_length = 15)
    blog = models.TextField(default = '')

    def __str__(self):
        return self.name
