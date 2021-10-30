from django.db import models

class User(models.Model):
    Name = models.CharField(max_length=50)
    Phone_Number = models.CharField(max_length=10)
class Request(models.Model):
    From = models.CharField(max_length=10)
    To  = models.CharField(max_length=10)
# Create your models here.
