from django.shortcuts import render,redirect
from django.views import View
from django import template
from service import path,session
from django.http import HttpResponse
from .data import mockContest
from django.contrib.auth.models import User
import sqlite3

# import random
# from django.core.files.storage import FileSystemStorage


# Create your views here.

def index(request):
    id = '1'
        #update Profile
    if request.method == 'POST':
        print("Update Profile comming soon")
        return
        

    haveError = False
        #Select Database
    try:
        conn = sqlite3.connect('./db.sqlite3')

        cmd = 'SELECT * FROM ContestAdmin_status JOIN ContestAdmin_contest ON ContestAdmin_status.IDcontest = ContestAdmin_contest.id JOIN ContestAdmin_language ON ContestAdmin_language.id = ContestAdmin_contest.IDLanguage WHERE ContestAdmin_status.IDUser = ' + id
        contestSubmited = conn.execute(cmd)
        
        cmd = 'SELECT * FROM ContestAdmin_account'
        contestRegisted = conn.execute(cmd)
        
        cmd = 'SELECT * FROM ContestAdmin_account'
        contestAll = conn.execute(cmd)
    except EOFError as e:
        print(e)
        haveError = True


    
        #Render Site
    dic = {'haveError': haveError, 'contestSubmited': contestSubmited, 'contestRegisted': contestRegisted, 'contestAll': contestAll}
    return render(request, 'ContestParticipant/index.html', dic)




def error(request):
    return render(request, 'ContestParticipant/error.html')


class ParticipantView(View):
    def get(self, request):
        if request.user.is_active:
            userName = str()
            try:
                userName = request.user.username
            except:
                userName = ''
            context = {
                'name': userName,
                'unRegisContests':mockContest,
                'regisContests': mockContest,
                'historyContests': mockContest,
            }
            return render(request, path.templateParticipant , context)
        else:
            #request.session['messAuth'] = 'Please Log In'
            return redirect('login')
    def post(self, request):
        #do sth
        return redirect('./')
class Register(View):
    def get(self, request, id):
        print(id)
        if request.user.is_active:
            userName = str()
            try:
                userName = request.user.username
            except:
                userName = ''
            context = {
                'name': userName,
                'registerStatus': 'Pending',
                'contest': mockContest[0]
            }
            return render(request, path.templateRegister , context)
        else:
            #request.session['messAuth'] = 'Please Log In'
            return redirect('login')

class Starting(View):
    def get(self, request, id):
        print(id)
        if request.user.is_active:
            userName = str()
            try:
                userName = request.user.username
            except:
                userName = ''
            context = {
                'name': userName,
                'registerStatus': 'Pending',
                'contest': mockContest[0], # selected by id
                'timeremaining': '70:00'
            }
            return render(request, path.templateStart , context)
        else:
            #request.session['messAuth'] = 'Please Log In'
            return redirect('login')
    def post(self, request,id):
        return redirect('/contest/status/'+id)

