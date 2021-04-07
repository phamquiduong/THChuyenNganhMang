from django.shortcuts import render
from django.views import View
from django import template
from . import models


class Login(View):
    template = 'login/login.html'

    def get(self, request):
        return render(request, self.template)


class SignUp(View):
    template = 'signUp/signUp.html'

    def get(self, request):
        return render(request, self.template)
