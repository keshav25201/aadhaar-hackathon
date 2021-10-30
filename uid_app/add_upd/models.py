from django.db import models

class Request(models.Model):
    From = models.CharField(max_length=10)
    To  = models.CharField(max_length=10)
# Create your models here.
