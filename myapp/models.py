from django.db import models

# Create your models here.
class feature(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=500)