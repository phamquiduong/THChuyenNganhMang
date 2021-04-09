from django.shortcuts import render,redirect
from django.views import View
from django import template
from . import models


templateLogin = 'login/login.html'
templateSignUp = 'signUp/signUp.html'
class Login(View):

    def get(self, request):
        return render(request, templateLogin)


class SignUp(View):

    def get(self, request):
        return render(request, templateSignUp)

    def post(seft, request):
        name = request.POST.get("name")
        userName = request.POST.get("userName")
        password = request.POST.get("password")
        try:
            p = models.Auth.objects.create(userName=userName, userDescription= name, password=password)
            p.save()
            context = {
                'mess':'Sign Up Success',
            }
            return render(request, templateLogin, context);
        except Exception as e:
            context = {
                'mess':'Sign Up Fail',
            }
            return render(request, templateSignUp, context)

