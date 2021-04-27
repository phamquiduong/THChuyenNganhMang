from django import forms
from django.contrib.auth import get_user_model
from django.forms.models import inlineformset_factory
import re
from django.utils.translation import ugettext_lazy as _
from django.forms import ValidationError

from .models import *
from django.contrib.auth.models import User
import hashlib

#     IDUser = models.CharField(max_length=100)
#     Title = models.TextField()
#     Description = models.TextField()
#     LinkContest = models.CharField(max_length=100)
#     LinkDataTrain = models.CharField(max_length=100)
#     LinkDataTest = models.CharField(max_length=100)
#     TimeRegister = models.DateTimeField()
#     TimeStart = models.DateTimeField()
#     TimeEnd = models.DateTimeField()
#     TimeOut = models.IntegerField()
#     IDLanguage = models.CharField(max_length=100)

# Language = models.CharField(max_length=100)
class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = [
            'Language',
        ]
        widgets = {
            'Language': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(LanguageForm, self).__init__(*args, **kwargs)
        
        if self.instance and self.instance.pk:
            self.fields['Language'].initial = self.instance.Language
            
            

class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = [
            'IDUser',
            'Title',
            'Description',
            'LinkContest',
            'LinkDataTrain',
            'LinkDataTest',
            'TimeRegister',
            'TimeStart',
            'TimeEnd',
            'TimeOut',
            'IDLanguage',
        ]
        widgets = {
            'IDUser': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'Title': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'Description': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'LinkContest': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'LinkDataTrain': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'LinkDataTest': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'TimeRegister': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'TimeStart': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'TimeEnd': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'TimeOut': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'IDLanguage': forms.TextInput(attrs={'required': True, 'class': 'form-control'}), 
        }
    
    def __init__(self, *args, **kwargs):
        super(ContestForm, self).__init__(*args, **kwargs)
        
        if self.instance and self.instance.pk:
            self.fields['IDUser'].initial = self.instance.IDUser
            self.fields['Title'].initial = self.instance.Title
            self.fields['Description'].initial = self.instance.Description
            self.fields['LinkDataTrain'].initial = self.instance.LinkDataTrain
            self.fields['LinkDataTest'].initial = self.instance.LinkDataTest
            self.fields['TimeRegister'].initial = self.instance.TimeRegister
            self.fields['TimeStart'].initial = self.instance.TimeStart
            self.fields['TimeEnd'].initial = self.instance.TimeEnd
            self.fields['TimeOut'].initial = self.instance.TimeOut
            self.fields['IDLanguage'].initial = self.instance.IDLanguage
            self.fields['LinkContest'].initial = self.instance.LinkContest
            
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'IDcontest',
            'IDUser',
            'Status',
            'TimeSubmit',
            'LinkSubmit',
        ]
        widgets = {
            'IDcontest': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'IDUser': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'Status': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'TimeSubmit': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'LinkSubmit': forms.TextInput(attrs={'required': True, 'class': 'form-control'})
        }
    
    def __init__(self, *args, **kwargs):
        super(StatusForm, self).__init__(*args, **kwargs)
        
        if self.instance and self.instance.pk:
            self.fields['IDcontest'].initial = self.instance.IDcontest
            self.fields['IDUser'].initial = self.instance.IDUser
            self.fields['Status'].initial = self.instance.Status
            self.fields['TimeSubmit'].initial = self.instance.TimeSubmit
            self.fields['LinkSubmit'].initial = self.instance.LinkSubmit

class UserForm(forms.ModelForm):
    class Meta:
        choice_t_f = [
            ('True', 'True'),
            ('False', 'False'),
        ]
        model = User
        fields = [
            'password',
            'username',
            'email',
            'is_superuser',
            'is_staff',
            'is_active'
        ]
        widgets = {
            'password': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'is_superuser': forms.Select(choices=choice_t_f, attrs={ 'required': True, 'class': 'form-control', 'default': 'False'}),
            'is_staff': forms.Select(choices=choice_t_f, attrs={ 'required': True, 'class': 'form-control', 'value': 'False'}),
            'is_active': forms.Select(choices=choice_t_f, attrs={ 'required': True, 'class': 'form-control', 'value': 'False'}),
            
        }
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        
        if self.instance and self.instance.pk:
            self.fields['password'].initial = self.instance.password
            self.fields['username'].initial = self.instance.username
            self.fields['email'].initial = self.instance.email
            self.fields['is_superuser'].initial = self.instance.is_superuser
            self.fields['is_staff'].initial = self.instance.is_staff
            self.fields['is_active'].initial = self.instance.is_active
    
