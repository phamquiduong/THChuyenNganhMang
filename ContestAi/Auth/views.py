from django.shortcuts import render,redirect, HttpResponse
from django.views import View
from django import template
from . import models
from service import path,session
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import re

class Login(View):

    def get(self, request):
        if request.user.is_authenticated == True:
            return redirect('../')
        else:
            return render(request, path.templateLogin)
    def post(self, request):
        us = request.POST.get("UserName")
        us = us.lower()
        regex = re.compile('[_!#$%^&*()<>?/|}{~:\s\'\"\[\]]')
        regex1 = re.compile('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
        if(regex.search(us) and not(regex1.search(us))):
            contest = {
                'mess': 'Ten dang nhap khong hop le'
            }
            return render(request, path.templateLogin, contest)
        else:
            pw = request.POST.get("PassWord")
            try:
                my_user = authenticate(request, username = User.objects.get(email = us).username, password = pw)
            except:
                my_user = authenticate(request, username = us, password = pw)
            if my_user is None:
                contest = {
                    'mess': 'Tai khoan dang nhap khong hop le'
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
        if request.user.is_authenticated == True:
            return redirect('../')
        else:
            return render(request, path.templateSignUp)

    def post(self, request):
        #name = request.POST.get("name")
        #userName = request.POST.get("userName")
        userName = request.POST.get("name")
        userName = userName.lower()
        regex = re.compile('[_!@#$%^&*()<>?/|}{~:\s\'\"\[\]]')
        regex1 = re.compile('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
        email = request.POST.get("email")
        password = request.POST.get("password")
        if (regex.search(userName)):
            contest = {
                'mess': 'Ten dang ki khong hop le'
            }
            return render(request, path.templateSignUp, contest)
        elif (User.objects.filter(username=userName)):
            contest = {
                'mess': 'Ten dang ki da ton tai'
            }
            return render(request, path.templateSignUp, contest)
        elif (not regex1.search(email)):
            contest = {
                'mess': 'Email dang ki khong hop le'
            }
            return render(request, path.templateSignUp, contest)
        elif (User.objects.filter(email=email)):
            contest = {
                'mess': 'Email dang ki da ton tai'
            }
            return render(request, path.templateSignUp, contest)
        else:
            user = User.objects.create_user(username=userName, email=email, password=password)
            user.is_active = True
            user.is_staff = False
            user.is_superuser = False
            user.save()
            return redirect('../login')
        #roleId = request.POST.get("role")
        #try:
            #request.session['messAuth'] = 'Sign Up Success'
            #return redirect('../login')
        #except Exception as e:
            #request.session['messAuth'] = 'Sign Up Fail'
            #return redirect('./')

class LogOut(View):
    def post(self, request):
        logout(request)
        return redirect('login')