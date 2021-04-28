from django.shortcuts import render,redirect
from django.views import View
from django import template
from service import path,session
from django.http import HttpResponse
#from .data import mockContest
from datetime import datetime
from ContestAdmin import models
import django_rq
import rq

def run_tester(s,path):
    import importlib
    import sys
    spec = importlib.util.spec_from_file_location('tester', path+'tester.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules['tester'] = module
    spec.loader.exec_module(module)
    obj = models.Status.objects.get(id=s)
    try:
        obj.Status=module.check_python(str(s))
    except rq.timeouts.JobTimeoutException:
        obj.Status="TLE"
    except:
        obj.Status="Compile Error"
    obj.save()

def run_tester_cpp(s,path):
    import importlib
    import sys
    spec = importlib.util.spec_from_file_location('tester', path+'tester.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules['tester'] = module
    spec.loader.exec_module(module)
    obj = models.Status.objects.get(id=s)
    try:
        obj.Status=module.check_cpp(str(s))
    except rq.timeouts.JobTimeoutException:
        obj.Status="TLE"
    except:
        obj.Status="Compile Error"
    obj.save()


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
                allContest = models.Contest.objects.all().order_by('-id')
                # print(allContest)

                idContestRegis = models.RegisterContest.objects.filter(IDUser=request.user.id).values_list('IDContest',flat=True) # contest that user regis before
                # print(list(idContestRegis))
                contestRegisted = []
                for id in list(idContestRegis):
                    contestRegisted.append(allContest.filter(id=id)[0])
                # print('contestRegisted',contestRegisted)
                
                allStatus = models.Status.objects.filter(IDUser=request.user.id).order_by('-id')
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
                
                # print(status)

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
        # print(id)
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
            # print(context)
            return render(request, path.templateStart , context)
        else:
            request.session['messAuth'] = 'Please Log In'
            return redirect('login')
    def post(self, request,id):
        # Check time Submit
        selectedContest = models.Contest.objects.get(id=id)
        time_end_string = selectedContest.TimeEnd.strftime("%Y-%m-%d %H:%M:%S")
        time_now = datetime.now()
        time_end = datetime.strptime(time_end_string,"%Y-%m-%d %H:%M:%S")
        if time_now > time_end:
            return redirect('/start/'+id)

        #  Submit
        f = request.FILES["file"]
        name = str(f)
        # print(name)
        path = './static/contest/contest'+str(id)+'/'
        if ".py" in name:
            obj = models.Status()
            obj.IDcontest = id
            obj.IDUser = request.user.id
            obj.Status = 'Pending'
            obj.TimeSubmit = datetime.now()
            obj.save()
            obj.LinkSubmit = path+str(obj.id)+'.py'
            obj.save()
            with open(obj.LinkSubmit, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            run_tester(obj.id,path)
            t = models.Contest.objects.get(id=id).TimeOut * 8
            # print(t)
            # queue = django_rq.get_queue('default',default_timeout=c)
            # queue.enqueue(run_tester,'test',result_ttl=0)   
        if ".cpp" in name:
            obj = models.Status()
            obj.IDcontest = id
            obj.IDUser = request.user.id
            obj.Status = 'Pending'
            obj.TimeSubmit = datetime.now()
            obj.save()
            obj.LinkSubmit = path+str(obj.id)+'.cpp'
            obj.save()
            with open(obj.LinkSubmit, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            run_tester_cpp(obj.id,path)
            t = models.Contest.objects.get(id=id).TimeOut * 8
            # print(t)
            # queue = django_rq.get_queue('default',default_timeout=c)
            # queue.enqueue(run_tester_cpp,'test',result_ttl=0)  
        return redirect('/contest/status/'+id)

class History(View):
    def get(self, request, id):
        if request.user.is_staff:
            userName = str()
            try:
                userName = request.user.username
            except:
                userName = ''
        selectedContest = models.Contest.objects.get(id=id)
        context = {
            'name': userName,
            'dataContests': selectedContest,
        }

        
        return render(request,path.templateHistorySubmit,context)