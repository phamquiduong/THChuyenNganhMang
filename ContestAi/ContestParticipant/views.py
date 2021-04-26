from django.shortcuts import render,redirect
from django.views import View
from django import template
from service import path,session
from django.http import HttpResponse
#from .data import mockContest
import sqlite3
from datetime import datetime

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
            try:
                userName = request.user.username
            except:
                userName = ''

            try:
                conn = sqlite3.connect('./db.sqlite3')

                cmd = "SELECT id FROM auth_user WHERE username='{}'".format(userName)
                data = conn.execute(cmd)
                for row in data:
                    id = row[0]
                print(data,id)

                cmd = "SELECT ContestAdmin_contest.id,ContestAdmin_contest.Title,ContestAdmin_contest.Description,ContestAdmin_contest.TimeRegister,ContestAdmin_contest.TimeStart,ContestAdmin_contest.TimeEnd,ContestAdmin_language.Language,ContestAdmin_status.Status FROM ContestAdmin_status JOIN ContestAdmin_contest ON ContestAdmin_status.IDcontest = ContestAdmin_contest.id JOIN ContestAdmin_language ON ContestAdmin_language.id = ContestAdmin_contest.IDLanguage WHERE ContestAdmin_status.IDUser = '{}' GROUP BY ContestAdmin_status.IDContest".format(id)
                submited = conn.execute(cmd)
        
                cmd = "SELECT ContestAdmin_contest.id,ContestAdmin_contest.Title,ContestAdmin_contest.Description,ContestAdmin_contest.TimeRegister,ContestAdmin_contest.TimeStart,ContestAdmin_contest.TimeEnd,ContestAdmin_language.Language FROM ContestAdmin_registercontest JOIN ContestAdmin_contest ON ContestAdmin_contest.id = ContestAdmin_registercontest.IDContest JOIN ContestAdmin_language ON ContestAdmin_contest.IDLanguage = ContestAdmin_language.id WHERE ContestAdmin_registercontest.IDUser='{0}' AND ContestAdmin_registercontest.IDcontest NOT IN (SELECT (IDcontest) FROM ContestAdmin_status WHERE IDUser = '{0}')".format(id)
                registed = conn.execute(cmd)
        
                cmd = "SELECT ContestAdmin_contest.id,ContestAdmin_contest.Title,ContestAdmin_contest.Description,ContestAdmin_contest.TimeRegister,ContestAdmin_contest.TimeStart,ContestAdmin_contest.TimeEnd,ContestAdmin_language.Language FROM ContestAdmin_contest JOIN ContestAdmin_language ON ContestAdmin_contest.IDLanguage = ContestAdmin_language.id WHERE ContestAdmin_contest.id NOT IN (SELECT (IDcontest) FROM ContestAdmin_registercontest WHERE ContestAdmin_registercontest.IDUser = '{0}')".format(id)
                unregisted = conn.execute(cmd)

            except Exception as e:
                print(e)

            historyContests=[]
            regisContests=[]
            unRegisContests=[]

            # print('\n\n\n-----------------------Sub contest')
            for row in submited:    
                t = {
                    "idContest": row[0],
                    "title": row[1],
                    "description": row[2],
                    "timeRegister": row[3],
                    "timeStart": row[4],
                    "timeEnd": row[5],
                    "language": row[6],
                    "result":row[7]
                }
                historyContests.append(t)
            # for x in historyContests: print(x)

            # print('\n\n\n-----------------------Regi contest')
            for row in registed:
                t = {
                    "idContest": row[0],
                    "title": row[1],
                    "description": row[2],
                    "timeRegister": row[3],
                    "timeStart": row[4],
                    "timeEnd": row[5],
                    "language": row[6],
                    "isRegister": True,
                }
                regisContests.append(t)
            # for x in regisContests: print(x)
    

            # print('\n\n\n-----------------------All contest')
            for row in unregisted:   
                t = {
                    "idContest": row[0],
                    "title": row[1],
                    "description": row[2],
                    "timeRegister": row[3],
                    "timeStart": row[4],
                    "timeEnd": row[5],
                    "language": row[6],
                    "isRegister": False,
                }
                unRegisContests.append(t)
            # for x in unRegisContests: print(x)
            
            context = {
                'name': userName,
                'unRegisContests':unRegisContests,
                'regisContests': regisContests,
                'historyContests': historyContests,
            }

            print(context)
            
            return render(request, path.templateParticipant , context)
        else:
            request.session['messAuth'] = 'Please Log In'
            return redirect('login')
    def post(self, request):
        #do sth
        return redirect('./')








class Register(View):
    def get(self, request, id):
        # print(id)
        if request.user.is_active:
            try:
                userName = request.user.username
            except:
                userName = ''
                
            try:
                conn = sqlite3.connect('./db.sqlite3')

                cmd = "SELECT id FROM auth_user WHERE username='{}'".format(userName)
                data = conn.execute(cmd)
                for row in data:
                    id_user = row[0]

                # print('id nguoi dung: ' + str(id_user))
                # print('id exam: ' + id)

                cmd = "SELECT TimeRegister FROM ContestAdmin_contest WHERE id = '{}'".format(id)
                data = conn.execute(cmd)
                for row in data:
                    time_reg_string = row[0]
                
                # print('time_reg: ' + time_reg_string)

                time_reg = datetime.strptime(time_reg_string,'%Y-%m-%d %H:%M:%S')

                time_now = datetime.now()

                if (time_reg>time_now):
                    cmd = "INSERT INTO ContestAdmin_registercontest(IDcontest,IDUser) VALUES ('{0}','{1}')".format(id,id_user)
                    conn.execute(cmd)
                    conn.commit()
                    status = 'OK'
                else:
                    status = 'Not time reg'

            except Exception as e:
                print(e)

            context = {
                'name': userName,
                'registerStatus': status,
                'contest': mockContest[0]
            }

            print(status)

            return render(request, path.templateRegister , context)
        else:
            request.session['messAuth'] = 'Please Log In'
            return redirect('login')
















class Starting(View):
    def get(self, request, id):
        print(id)
        if request.user.is_active:
            try:
                userName = request.user.username
            except:
                userName = ''

            try:
                conn = sqlite3.connect('./db.sqlite3')

                cmd = "SELECT id FROM auth_user WHERE username='{}'".format(userName)
                data = conn.execute(cmd)
                for row in data:
                    id_user = row[0]

                # print('id nguoi dung: ' + str(id_user))
                # print('id exam: ' + id)

                cmd = "SELECT TimeStart,TimeEnd FROM ContestAdmin_contest WHERE id = '{}'".format(id)
                data = conn.execute(cmd)
                for row in data:
                    time_start_string = row[0]
                    time_end_string = row[1]
                
                # print('time_reg: ' + time_reg_string)

                time_start = datetime.strptime(time_start_string,'%Y-%m-%d %H:%M:%S')
                time_end = datetime.strptime(time_end_string,'%Y-%m-%d %H:%M:%S')

                time_now = datetime.now()

                if (time_start<time_now and time_now<time_end):
                    status = 'OK'
                else:
                    status = 'Not time to test'
                    
            except Exception as e:
                print(e)

            context = {
                'name': userName,
                'registerStatus': status,
                'contest': mockContest[0], # selected by id
                'timeremaining': '70:00'
            }
            return render(request, path.templateStart , context)
        else:
            request.session['messAuth'] = 'Please Log In'
            return redirect('login')
    def post(self, request,id):
        return redirect('/contest/status/'+id)