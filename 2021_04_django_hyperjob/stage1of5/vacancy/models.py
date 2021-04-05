from django.db import models
from django.conf import settings

# Create your models here.
class Vacancy(models.Model):
  description = models.CharField(max_length=1024)                                 ##  self explanatory
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    ##  no idea where settings.AUTH_USER_MODEL came from
