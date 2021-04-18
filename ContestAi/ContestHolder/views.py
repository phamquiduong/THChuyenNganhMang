from django.shortcuts import render,redirect
from django.views import View
from django import template
from service import path,session
from .data import mockData, mockUser, mockStatus
from ContestAdmin import models
import os

class HolderView(View):
    def get(self, request):
        if session.isAuthenticated(request):
            userName = str()
            try:
                userName = request.session.get('user')['name']
            except:
                userName = ''
            obj = models.Contest.objects.filter(IDUser=request.session.get('user')['id'])
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
            request.session['messAuth'] = 'Please Log In'
            return redirect('login')

class ContestDetail(View):
    def get(self, request,id):
        if session.isAuthenticated(request):
            userName = str()
            try:
                userName = request.session.get('user')['name']
            except:
                userName = ''
            detailData = models.Contest.objects.filter(id=id)
            context = {
                'name': userName,
                'dataContests': detailData,
                'listParticipants': mockUser
            }
            return render(request, path.templateDetail, context)
        else:
            request.session['messAuth'] = 'Please Log In'
            return redirect('login')
    def post(self, request,id):
        try:
            content = request.FILES['content']
            kt_content = True
        except:
            kt_content = False
        try:
            train = request.FILES['train']
            print("OK")
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
        if session.isAuthenticated(request):
            userName = str()
            try:
                userName = request.session.get('user')['name']
            except:
                userName = ''
            context = {
                'name': userName,
            }
            return render(request, path.templateCreate, context)
        else:
            request.session['messAuth'] = 'Please Log In'
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
            obj.IDUser = request.session.get('user')['id']
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
        selectedContest = list(filter(lambda x: id == x['idContest'], mockData))
        context = {
            'dataContests': selectedContest,
            'dataStatus': mockStatus
        }

        if session.isAuthenticated(request):
            userName = str()
            try:
                userName = request.session.get('user')['name']
            except:
                userName = ''
            context['name'] = userName
        
        return render(request,path.templateStatus,context)