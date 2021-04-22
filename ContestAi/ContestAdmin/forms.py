from django import forms
from django.contrib.auth import get_user_model
from django.forms.models import inlineformset_factory
import re
from django.utils.translation import ugettext_lazy as _
from django.forms import ValidationError

from .models import *


class StaticForm(forms.ModelForm):

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
        super(StaticForm, self).__init__(*args, **kwargs)
        
        if self.instance and self.instance.pk:
            self.fields['IDcontest'].initial = self.instance.IDcontest
            self.fields['IDUser'].initial = self.instance.IDUser
            self.fields['Status'].initial = self.instance.Status
            self.fields['TimeSubmit'].initial = self.instance.TimeSubmit
            self.fields['LinkSubmit'].initial = self.instance.LinkSubmit

    