from django.shortcuts import render,redirect
from django.views import View
from django import template
from . import models
from service import path,session
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import re


class Login(View):

    def get(self, request):
        if request.user.is_superuser:
            return redirect('/account/')
        elif request.user.is_staff:
            return redirect('/holder/')
        elif request.user.is_active:
            return redirect('/participant/')
        else:
            contest = {
                'mess': 'Moi ban dang nhap de vao trang web'
            }
            return render(request, path.templateLogin, contest)
    def post(self, request):
        userName = request.POST.get("userName").lower()
        regex = re.compile('[_!#$%^&*()<>?/|}{~:\s\'\"\[\]]')
        regex1 = re.compile('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
        if (regex.search(userName) and not(regex1.search(userName))):
            contest = {
                'mess': 'Ten dang nhap hoac email khong hop le'
            }
            return render(request, path.templateLogin, contest)
        else:
            password = request.POST.get("password")
            try:
                my_user = authenticate(request, username = User.objects.get(email = userName).username, password = password)
            except:
                my_user = authenticate(request, username = userName, password = password)
            if my_user is None:
                contest = {
                    'mess': 'Tai khoan dang nhap khong hop le'
                }
                return render(request, path.templateLogin, contest)
            else:
                login(request,my_user)
                if request.user.is_superuser == True:
                    return redirect('/account/')
                elif request.user.is_staff == True:
                    return redirect('/holder/')
                elif request.user.is_active == True:
                    return redirect('/participant/')


class SignUp(View):
    
    def get(self, request):
        if request.user.is_superuser:
            return redirect('/account/')
        elif request.user.is_staff:
            return redirect('/holder/')
        elif request.user.is_active:
            return redirect('/participant/')
        else:
            return render(request, path.templateSignUp)

    def post(self, request):
        userName = request.POST.get("name").lower()
        regex = re.compile('[_!@#$%^&*()<>?/|}{~:\s\'\"\[\]]')
        regex1 = re.compile('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
        email = request.POST.get("email").lower()
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
            return redirect('/login/')
class LogOut(View):
    def post(self, request):
        logout(request)
        return redirect('/login/')
