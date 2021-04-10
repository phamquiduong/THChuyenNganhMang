from django.shortcuts import render,redirect
from django.views import View
from django import template
from . import models



templateLogin = 'login/login.html'
templateSignUp = 'signUp/signUp.html'
templateHolder =  'holder/index.html'

class Login(View):

    def get(self, request):
        messAuth = str()
        try:
            messAuth = request.session.get('messAuth')
            del request.session['messAuth']
        except:
            messAuth = ''
        context = {
            'mess': messAuth,
        }
        return render(request, templateLogin, context)
    
    def post(seft, request):
        userName = request.POST.get("userName")
        password = request.POST.get("password")
        request.session['user'] = {
            'name' : userName,
        }
        #do sth 
        #case success login
        return redirect('../holder')



class SignUp(View):

    def get(self, request):
        messAuth = str()
        try:
            messAuth = request.session.get('messAuth')
            del request.session['messAuth']
        except:
            messAuth = ''
        context = {
            'mess': messAuth,
        }
        return render(request, templateSignUp, context)

    def post(seft, request):
        name = request.POST.get("name")
        userName = request.POST.get("userName")
        password = request.POST.get("password")
        try:
            p = models.Auth.objects.create(userName=userName, userDescription= name, password=password)
            p.save()
            request.session['messAuth'] = 'Sign Up Success'
            return redirect('../login')
        except Exception as e:
            request.session['messAuth'] = 'Sign Up Fail'
            return redirect('./')

class LogOut(View):
    def post(self, request):
        print("catch logout")
        try:
            request.session['messAuth'] = 'Log Out Success'
            del request.session['user']
        except:
            request.session['messAuth'] = 'Log Out Fail'
            return redirect('../login')
        return redirect('../login')