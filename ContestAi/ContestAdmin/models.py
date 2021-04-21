from django.db import models

# Create your models here.
class Account(models.Model):
    UserName = models.CharField(unique=True, max_length=100, default='')
    Password = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Permission = models.CharField(max_length=100)

class Contest(models.Model):
    IDUser = models.CharField(max_length=100)
    Title = models.TextField()
    Description = models.TextField()
    LinkContest = models.CharField(max_length=100)
    LinkDataTrain = models.CharField(max_length=100)
    LinkDataTest = models.CharField(max_length=100)
    LinkTester = models.CharField(max_length=100)
    TimeRegister = models.DateTimeField()
    TimeStart = models.DateTimeField()
    TimeEnd = models.DateTimeField()
    TimeOut = models.IntegerField()
    IDLanguage = models.CharField(max_length=100)

class Status(models.Model):
    IDcontest = models.CharField(max_length=100)
    IDUser = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    TimeSubmit = models.DateTimeField()
    LinkSubmit = models.CharField(max_length=100)
    def __str__(self):
        return self.IDcontest
    

class RegisterContest(models.Model):
    IDContest = models.CharField(max_length=100)
    IDUser = models.CharField(max_length=100)

class Language(models.Model):
    Language = models.CharField(max_length=100)