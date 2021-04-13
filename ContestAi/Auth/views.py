from django.shortcuts import render,redirect, HttpResponse
from django.views import View
from django import template
from . import models
from service import path,session
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class Login(View):

    def get(self, request):
        if request.user.is_authenticated == True:
            logout(request)
        return render(request, path.templateLogin)
    def post(self, request):
        us = request.POST.get("UserName")
        pw = request.POST.get("PassWord")
        my_user = authenticate(request, username = User.objects.get(email = us).username, password = pw)
        if my_user is None:
            contest = {
                'mess': 'Tai khoan khong hop le'
            }
            return render(request, path.templateLogin, contest)
        else:
            login(request,my_user)
            if request.user.is_superuser == True:
                return HttpResponse('Welcome'+request.user.username)
            elif request.user.is_staff == True:
                return HttpResponse('Hello'+request.user.username)
            elif request.user.is_active == True:
                return HttpResponse('Hi'+request.user.username) 


class SignUp(View):

    def get(self, request):
        if not session.isAuthenticated(request):
            messAuth = str()
            try:
                messAuth = request.session.get('messAuth')
                del request.session['messAuth']
            except:
                messAuth = ''
            context = {
                'mess': messAuth,
            }
            return render(request, path.templateSignUp, context)
        else:
            return redirect('holder')

    def post(self, request):
        name = request.POST.get("name")
        userName = request.POST.get("userName")
        password = request.POST.get("password")
        roleId = request.POST.get("role")
        try:
            
            request.session['messAuth'] = 'Sign Up Success'
            return redirect('../login')
        except Exception as e:
            request.session['messAuth'] = 'Sign Up Fail'
            return redirect('./')

class LogOut(View):
    def post(self, request):
        logout(request)
        return redirect('login')