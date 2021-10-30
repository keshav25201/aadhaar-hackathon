from django.db import models
import uuid
class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    From = models.CharField(max_length=10)
    To  = models.CharField(max_length=10)
# Create your models here.
