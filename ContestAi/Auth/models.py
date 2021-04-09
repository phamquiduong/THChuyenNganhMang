from django.db import models

# Create your models here.

class Auth (models.Model):
    userName = models.CharField(max_length=50, primary_key=True)
    userDescription = models.CharField(max_length=50)
    password =  models.CharField(max_length=50)
