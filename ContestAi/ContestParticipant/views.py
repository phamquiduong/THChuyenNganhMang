from django.shortcuts import render,redirect
from django.views import View
from django import template
from service import path,session
from django.shortcuts import render
from django.http import HttpResponse
import sqlite3

# import random
# from django.core.files.storage import FileSystemStorage


# Create your views here.

def index(request):
    id = '1'
        #update Profile
    if request.method == 'POST':
        print("Update Profile comming soon")

    haveError = False
        #Select Database
    try:
        conn = sqlite3.connect('./db.sqlite3')

        cmd = 'SELECT * FROM ContestAdmin_status JOIN ContestAdmin_contest ON ContestAdmin_status.IDcontest = ContestAdmin_contest.id JOIN ContestAdmin_language ON ContestAdmin_language.id = ContestAdmin_contest.IDLanguage WHERE ContestAdmin_status.IDUser = ' + id
        contestSubmited = conn.execute(cmd)
        
        cmd = 'SELECT * FROM ContestAdmin_registercontest JOIN ContestAdmin_contest ON ContestAdmin_contest.id = ContestAdmin_registercontest.IDContest JOIN ContestAdmin_language ON ContestAdmin_contest.IDLanguage = ContestAdmin_language.id WHERE ContestAdmin_registercontest.IDUser = ' + id + ' AND ContestAdmin_registercontest.IDcontest NOT IN (SELECT (IDcontest) FROM ContestAdmin_status WHERE IDUser = ' + id + ')'
        contestRegisted = conn.execute(cmd)
        
        cmd = 'SELECT * FROM ContestAdmin_contest JOIN ContestAdmin_language ON ContestAdmin_contest.IDLanguage = ContestAdmin_language.id WHERE ContestAdmin_contest.id NOT IN (SELECT (IDcontest) FROM ContestAdmin_registercontest WHERE ContestAdmin_registercontest.IDUser = ' + id + ')'
        contestAll = conn.execute(cmd)

        cmd = 'SELECT username, last_name, first_name FROM auth_user WHERE id=' + id
        for row in conn.execute(cmd):
            infoUser = row

    except EOFError as e:
        print(e)
        haveError = True

        #Render Site
    dic = {'id': id, 'infoUser': infoUser, 'haveError': haveError, 'contestSubmited': contestSubmited, 'contestRegisted': contestRegisted, 'contestAll': contestAll}
    return render(request, 'ContestParticipant/index.html', dic)


class ParticipantView(View):
    def get(self, request):
        if session.isAuthenticated(request):
            userName = str()
            try:
                userName = request.session.get('user')['name']
            except:
                userName = ''
            context = {
                'name': userName,
                'listContext':[],
            }
            return render(request, path.templateParticipant , context)
        else:
            request.session['messAuth'] = 'Please Log In'
            return redirect('login')
    def post(self, request):
        #do sth
        return redirect('./')
