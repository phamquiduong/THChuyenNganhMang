from django import forms
from django.contrib.auth import get_user_model
from django.forms.models import inlineformset_factory
import re
from django.utils.translation import ugettext_lazy as _
from django.forms import ValidationError

from .models import *
from django.contrib.auth.models import User
import hashlib

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
    
    # def clean(self):
    #     password = self.cleaned_data['password']
    #     password = hashlib.sha256(password).hexdigest()
    #     # product = self.cleaned_data['product']
    #     # available = product.get_balance_stock()
    #     # if self.cleaned_data['quantity'] > available:
    #     #     raise forms.ValidationError("You can't take out more stock of {} than is available ({})".format(product, available)