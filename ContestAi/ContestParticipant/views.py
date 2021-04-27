from django.shortcuts import render,redirect
from django.views import View
from django import template
from service import path,session
from django.http import HttpResponse
#from .data import mockContest
import sqlite3
from datetime import datetime
from ContestAdmin import models


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
                userId = request.user.id
            except:
                userName = ''
                userId = 0
            try:

                id = userId
                allContest = models.Contest.objects.all()
                # print(allContest)

                idContestRegis = models.RegisterContest.objects.filter(IDUser=request.user.id).values_list('IDContest',flat=True) # contest that user regis before
                # print(list(idContestRegis))
                contestRegisted = []
                for id in list(idContestRegis):
                    contestRegisted.append(allContest.filter(id=id)[0])
                # print('contestRegisted',contestRegisted)
                
                allStatus = models.Status.objects.filter(IDUser=request.user.id)
                idContestSubmitted = allStatus.values_list('IDcontest',flat=True) # contest that user regis before
                statusContestSubmitted = allStatus.values_list('Status',flat=True)
                contestSubmitted = []
                index = 0
                for id in list(idContestSubmitted):
                    selected = allContest.filter(id=id)[0]
                    selected.Result = statusContestSubmitted[index]
                    contestSubmitted.append(selected)
                    index += 1
                # print('contestSubmitted',contestSubmitted)
                
                contestUnRegisted = []
                for contest in allContest:
                    if contest not in contestRegisted and contest not in contestSubmitted:
                        contestUnRegisted.append(contest)
                # print('contestUnRegisted', contestUnRegisted)

            except Exception as e:
                print(e)

            context = {
                'name': userName,
                'unRegisContests':list(contestUnRegisted),
                'regisContests':list(contestRegisted),
                'historyContests': list(contestSubmitted),
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
        if request.user.is_active:
            try:
                userName = request.user.username
                userId = request.user.id
            except:
                userName = ''
                userId = ''
            try:


                selectedContest = models.Contest.objects.get(id=id)
                time_reg_string = selectedContest.TimeRegister.strftime("%Y-%m-%d %H:%M:%S")
                time_start_string = selectedContest.TimeStart.strftime("%Y-%m-%d %H:%M:%S")
                time_now = datetime.now()
                

                time_reg = datetime.strptime(time_reg_string,"%Y-%m-%d %H:%M:%S")
                time_start = datetime.strptime(time_start_string,"%Y-%m-%d %H:%M:%S")

                status = ''
                if time_now > time_reg and time_now < time_start:
                    try:
                        regisTemplate = models.RegisterContest(IDContest=id,IDUser=userId)
                        regisTemplate.save()
                        status = 'OK'
                    except Exception as e:
                        print(e)
                        status = 'FAIL'
                else:
                    status = 'PENDING'
                
                print(status)

            except Exception as e:
                print(e)

            context = {
                'name': userName,
                'registerStatus': status,
                'contest': selectedContest
            }


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
                userId = request.user.id
            except:
                userName = ''
                userId = ''

            try:

                
                selectedContest = models.Contest.objects.get(id=id)
                time_start_string = selectedContest.TimeStart.strftime("%Y-%m-%d %H:%M:%S")
                time_end_string = selectedContest.TimeEnd.strftime("%Y-%m-%d %H:%M:%S")
                time_now = datetime.now()

                time_start = datetime.strptime(time_start_string,"%Y-%m-%d %H:%M:%S")
                time_end = datetime.strptime(time_end_string,"%Y-%m-%d %H:%M:%S")


                if time_now < time_start:
                    status = 'PENDING'
                else:
                    if time_now > time_end:
                        status = 'EXPIRED' 
                    else:
                        status = 'OK'
                    
            except Exception as e:
                print(e)
            context = {
                'name': userName,
                'startStatus': status,
                'contest': selectedContest, # selected by id
                'timeEnd': selectedContest.TimeEnd.strftime("%m/%d/%Y %H:%M:%S"),
                'timeStart': selectedContest.TimeStart.strftime("%m/%d/%Y %H:%M:%S")
            }
            print(context)
            return render(request, path.templateStart , context)
        else:
            request.session['messAuth'] = 'Please Log In'
            return redirect('login')
    def post(self, request,id):
        return redirect('/contest/status/'+id)
