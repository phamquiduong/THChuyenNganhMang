from django.shortcuts import render,redirect
from django.views import View
from django import template
from service import path,session
from .data import mockData, mockUser, mockStatus
from ContestAdmin import models
from django.contrib.auth.models import User
import os

class HolderView(View):
    def get(self, request):
        if request.user.is_staff:
            try:
                userName = request.user.username
            except:
                userName = ''
            obj = models.Contest.objects.filter(IDUser=request.user.id).order_by('-id')
            # import datetime
            # now = datetime.datetime.now(obj[1].TimeStart.tzinfo)
            # if obj[1].TimeStart > now:
            #     print("YES")
            context = {
                'name': userName,
                'dataContests': obj,
            }
            return render(request, path.templateHolder , context)
        else:
            return redirect('login')

class ContestDetail(View):
    def get(self, request,id):
        if request.user.is_staff:
            userName = str()
            try:
                userName = request.user.username
            except:
                userName = ''
            detailData = models.Contest.objects.filter(id=id)
            data = []
            obj = models.RegisterContest.objects.filter(IDContest=id).order_by('-id')
            for x in obj:
                tg = {
                    'name' : User.objects.get(id=x.IDUser).username
                }
                data.append(tg)
            context = {
                'name': userName,
                'dataContests': detailData,
                'listParticipants': data
            }
            return render(request, path.templateDetail, context)
        else:
            return redirect('login')
    def post(self, request,id):
        try:
            content = request.FILES['content']
            kt_content = True
        except:
            kt_content = False
        try:
            train = request.FILES['train']
            kt_train = True
        except:
            kt_train = False
        try:
            test = request.FILES['test']
            kt_test = True
        except:
            kt_test = False
        try:
            tester = request.FILES['tester']
            kt_tester = True
        except:
            kt_tester = False
        obj = models.Contest.objects.get(id=id)
        obj.Title = request.POST.get('title')
        obj.Description = request.POST.get('description')
        obj.TimeRegister = request.POST.get('dateRegister')+' '+request.POST.get('timeRegister')
        obj.TimeStart = request.POST.get('dateStart')+' '+request.POST.get('timeStart')
        obj.TimeEnd = request.POST.get('dateEnd')+' '+request.POST.get('timeEnd')
        obj.TimeOut = request.POST.get('timeOut')
        obj.save()
        if kt_content == True:
            with open(obj.LinkContest, 'wb+') as destination:
                for chunk in content.chunks():
                    destination.write(chunk)
        if kt_train == True:
            with open(obj.LinkDataTrain, 'wb+') as destination:
                for chunk in train.chunks():
                    destination.write(chunk)
        if kt_test == True:           
            with open(obj.LinkDataTest, 'wb+') as destination:
                for chunk in test.chunks():
                    destination.write(chunk)
        if kt_tester == True:  
            with open(obj.LinkTester, 'wb+') as destination:
                for chunk in tester.chunks():
                    destination.write(chunk)
        return redirect('holder')

class ContestDelete(View):
    def get(self, request,id):
        print(id)
        obj = models.Contest.objects.get(id=id)
        obj.delete()
        return redirect('holder')
        
class CreateContest(View):
    def get(self, request):
        if request.user.is_staff:
            userName = str()
            try:
                userName = request.user.username
            except:
                userName = ''
            context = {
                'name': userName,
            }
            return render(request, path.templateCreate, context)
        else:
            return redirect('login')
    def post(self, request):
        try:
            content = request.FILES['content']
            train = request.FILES['train']
            test = request.FILES['test']
            tester = request.FILES['tester']
        except:
            return redirect('create')
        timeout = request.POST.get('timeOut')
        try:
            obj = models.Contest()
            obj.IDUser = request.user.id
            obj.Title = request.POST.get('title')
            obj.Description = request.POST.get('description')
            obj.TimeRegister = request.POST.get('dateRegister')+' '+request.POST.get('timeRegister')
            obj.TimeStart = request.POST.get('dateStart')+' '+request.POST.get('timeStart')
            obj.TimeEnd = request.POST.get('dateEnd')+' '+request.POST.get('timeEnd')
            obj.TimeOut = request.POST.get('timeOut')
            obj.save()
            id = str(obj.id)
        except:
            return redirect('create')
        path = './static/contest/contest'+id
        if not os.path.exists(path):
            os.makedirs(path)
        obj.LinkContest = path+'/content.pdf'
        obj.LinkDataTest = path+'/data_test.txt'
        obj.LinkDataTrain = path+'/data_train.txt'
        obj.LinkTester = path+'/tester.py'
        obj.save()
        with open(obj.LinkContest, 'wb+') as destination:
            for chunk in content.chunks():
                destination.write(chunk)
        with open(obj.LinkDataTrain, 'wb+') as destination:
            for chunk in train.chunks():
                destination.write(chunk)
        with open(obj.LinkDataTest, 'wb+') as destination:
            for chunk in test.chunks():
                destination.write(chunk)
        with open(obj.LinkTester, 'wb+') as destination:
            for chunk in tester.chunks():
                destination.write(chunk)
        return redirect('holder')

#############################PUBLIC###################
class ContestStatus(View):
    def get(self, request,id):
        status = models.Status.objects.filter(IDcontest = id).order_by('-id')
        data = []
        for x in status:
            language = "Error"
            if ".py" in x.LinkSubmit:
                language = 'Python'
            elif ".cpp" in x.LinkSubmit:
                language = 'C++'
            elif ".java" in x.LinkSubmit:
                language = 'Java'
            code = ''
            try:
                with open(x.LinkSubmit, 'r+') as destination:
                    for line in destination:
                        code = code + line
            except:
                code+='File not found'
            tg = {
                'iduser' : x.id,
                'name' : User.objects.get(id = x.IDUser).username,
                'time' : str(x.TimeSubmit),
                'language' : language,
                'status' : x.Status,
                'link' : x.LinkSubmit,
                'code' :code
            }
            data.append(tg)
        # for x in data:
        #     print(x)
        selectedContest = models.Contest.objects.filter(id = id)
        context = {
            'name': request.user.username,
            'dataContests': selectedContest,
            'dataStatus': data
        }
        # print(context)
        return render(request,path.templateStatus,context)