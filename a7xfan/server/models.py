import email
from django.db import models

class Data(models.Model):
   username = models.CharField(max_length=40)
   email = models.CharField(max_length=40)
   password = models.CharField(max_length=40)

class POST(models.Model):
   username = models.CharField(max_length=40)
   post = models.CharField(max_length=500)