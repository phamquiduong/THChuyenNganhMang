from django.shortcuts import render,redirect
from django.views import View
from django import template
from service import path,session
from .data import mockData, mockUser, mockStatus
from . import models

class HolderView(View):
    def get(self, request):
        if session.isAuthenticated(request):
            userName = str()
            try:
                userName = request.session.get('user')['name']
            except:
                userName = ''
            context = {
                'name': userName,
                'dataContests': mockData,
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
            detailData = list(filter(lambda x: id == x['idContest'], mockData))
            context = {
                'name': userName,
                'dataContests': detailData,
                'linkContest': 'demo/Contest1.pdf',
                'linkDataTrain': 'demo/test1.txt',
                'inRegis': 80,
                'inTodo': 53,
                'inResult':69,
                'listParticipants': mockUser
            }
            return render(request, path.templateDetail, context)
        else:
            request.session['messAuth'] = 'Please Log In'
            return redirect('login')
    def post(self, request,id):
        title = request.POST.get("title")
        description = request.POST.get("description")
        dateStart = request.POST.get("dateStart")
        timeStart = request.POST.get("timeStart")
        return redirect('holder')

class ContestDelete(View):
    def get(self, request,id):
        print(id)
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
        # title = request.POST.get('title')
        # dec = request.POST.get('description')
        # content = request.FILES['content']
        # train = request.FILES['train']
        # # test = request.FILES['test']
        # # tester = request.FILES['tester']
        print("h1")
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